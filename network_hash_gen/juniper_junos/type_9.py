from typing import Dict, List, Optional, Tuple

from network_hash_gen.utils import _generate_salt


class Type9:
    """
    The JunOS Type 9 password obfuscation algorithm.

    It is used to store passwords in the configuration that need to be
    available in plaintext, but should not be easily read by humans.
    For example passwords for BGP sessions.

    This is not a secure hash function!

    This implementation is based on code from
    https://github.com/msuksong/junosdecode/blob/master/junosdecode.py
    """

    __MAGIC = "$9$"

    __FAMILY: List[str] = [
        "QzF3n6/9CAtpu0O",
        "B1IREhcSyrleKvMW8LXx",
        "7N-dVbwsY2g4oaJZGUDj",
        "iHkq.mPf5T",
    ]
    # maps single characters to numbers from 0 to 3 (incl.)
    __EXTRA: Dict[str, int] = dict()
    for x, item in enumerate(__FAMILY):
        for c in item:
            __EXTRA[c] = 3 - x

    # List of 65 character, in sorted order they are:
    # -./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
    __NUM_ALPHA: str = "".join(__FAMILY)

    # reverse mapping from __NUM_ALPHA
    __ALPHA_NUM: Dict[str, int] = {x: i for (i, x) in enumerate("".join(__FAMILY))}

    # encoding moduli by position
    __ENCODING = [
        [1, 4, 32],
        [1, 16, 32],
        [1, 8, 32],
        [1, 64],
        [1, 32],
        [1, 4, 16, 128],
        [1, 32, 64],
    ]

    @staticmethod
    def encode(plaintext: str) -> str:
        """
        Encoded the given plaintext.
        Generates a random salt.
        """
        salt = Type9._generate_salt(length=1)
        return Type9.encode_salted(plaintext, salt)

    @staticmethod
    def encode_seeded(plaintext: str, seed: str) -> str:
        salt = Type9._generate_salt(length=1, seed=seed)
        return Type9.encode_salted(plaintext, salt)

    @staticmethod
    def encode_salted(plaintext: str, salt: str) -> str:
        """
        Encodes the given plaintext.
        """
        assert len(salt) == 1
        assert salt in Type9.__NUM_ALPHA

        # an additional, random string of length 0 to 3 (incl.)
        rand: str = Type9._generate_salt(Type9.__EXTRA[salt], seed=salt)

        position: int = 0
        prev: str = salt
        crypt = Type9.__MAGIC + salt + rand

        for x in plaintext:
            moduli = Type9.__ENCODING[position % len(Type9.__ENCODING)]
            crypt += Type9._gap_encode(x, prev, moduli)
            prev = crypt[-1]
            position += 1

        return crypt

    @staticmethod
    def decode(secret: str) -> str:
        """
        Decodes the given secret.
        """

        splits: List[str] = secret.split("$")
        assert len(splits) == 3

        magic: str = splits[1]
        assert magic == "9"

        encoding: str = splits[2]

        salt: str = encoding[0]

        rand_length: int = Type9.__EXTRA[salt]
        crypt: str = encoding[1 + rand_length :]

        input_position: int = 0

        prev: str = salt

        output: str = ""
        while input_position < len(crypt):
            moduli: List[int] = Type9.__ENCODING[len(output) % len(Type9.__ENCODING)]
            assert input_position + len(moduli) <= len(crypt)

            # the 2 to 4 characters that define the next output character
            enc: str = crypt[input_position : input_position + len(moduli)]

            gaps: List[int] = list()
            for character in enc:
                gap = Type9.__ALPHA_NUM[character] - Type9.__ALPHA_NUM[prev] - 1
                gap %= len(Type9.__NUM_ALPHA)
                gaps.append(gap)
                prev = character

            result = 0
            for i, gap in enumerate(gaps):
                result += gap * moduli[i]

            output += chr(result)

            input_position += len(moduli)

        return output

    @staticmethod
    def _gap_encode(pc: str, prev: str, moduli: List[int]):
        """
        pc is the plaintext byte,
        prev is the previous encoding,
        moduli is a list of moduli.
        """
        assert len(pc) == 1
        assert len(prev) == 1

        _ord = ord(pc)  # Unicode value of that character

        crypt: str = ""
        gaps: List = []

        # builds a encoding based on the given module.
        # with moduli [1, 2, 4, 8, ...] this would be binary encoding.
        # with moduli [1, 16, 256] it would be hexadecimal
        # but in this case each position can have a different value
        for mod in reversed(moduli):
            gaps.insert(0, int(_ord / mod))
            _ord %= mod

        for gap in gaps:
            gap += Type9.__ALPHA_NUM[prev] + 1
            prev = Type9.__NUM_ALPHA[gap % len(Type9.__NUM_ALPHA)]
            crypt += prev

        assert len(crypt) == len(moduli)
        return crypt

    @staticmethod
    def _parse_encoding(secret: str) -> Tuple[str, str, str]:
        """
        Returns a tuple containing the salt, rand and the encoded part
        of the given secret
        """
        splits: List[str] = secret.split("$")
        assert len(splits) == 3

        magic: str = splits[1]
        assert magic == "9"

        encoding: str = splits[2]

        salt: str = encoding[0]

        rand_length: int = Type9.__EXTRA[salt]
        rand: str = encoding[1 : 1 + rand_length]
        crypt: str = encoding[1 + rand_length :]

        return salt, rand, crypt

    @staticmethod
    def _generate_salt(length: int, seed: Optional[str] = None) -> str:
        return _generate_salt("".join(Type9.__NUM_ALPHA), length, seed)
