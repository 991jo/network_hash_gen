from typing import ByteString, Optional
import random
import scrypt
import base64

std_b64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
cisco_b64chars = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
b64table = str.maketrans(std_b64chars, cisco_b64chars)


def type_9_hash_salted(password: ByteString, salt: ByteString) -> ByteString:
    """
    Calculates a Cisco IOS/IOS-XE Type 9 hash with the given password and salt.
    """
    salt_str = salt.decode()

    # Create the hash
    hash = scrypt.hash(password.decode(), salt_str, 16384, 1, 1, 32)

    # Convert the hash from Standard Base64 to Cisco Base64
    hash = base64.b64encode(hash).decode().translate(b64table)[:-1]

    return bytearray(f"$9${salt_str}${hash}", encoding="utf-8")


def _generate_type_9_salt(seed: Optional[str] = None) -> ByteString:
    """
    Generates a salt for Cisco IOS type 9 hashes.

    If `seed` is specified the value is used to initialize the random number
    generator.
    """

    # initialize a seperate RNG to no seed the global instance used by the
    # functions called directly on the random module.
    rng = random.Random()

    if seed is not None:
        rng.seed(seed)

    # Create random salt (Cisco use 14 characters from custom B64 table)
    output = ""
    for _ in range(14):
        output += rng.choice(cisco_b64chars)

    return bytearray(output, encoding="utf-8")


def type_9_hash_seeded(password: ByteString, seed: str) -> ByteString:
    """
    Calculates a Cisco IOS/IOS-XE Type 9 hash with the given seed used for
    generating a appropriate salt.

    Use this function if you have to generate a password multiple times (e.g.
    when generating configs) to generate the same hash every time.
    """
    salt = _generate_type_9_salt(seed)
    return type_9_hash_salted(password, salt)


def type_9_hash(password: ByteString) -> ByteString:
    """
    Calculates a Cisco IOS/IOS-XE Type 9 hash.

    An appropriate salt is chosen randomly.
    """
    salt = _generate_type_9_salt()
    return type_9_hash_salted(password, salt)
