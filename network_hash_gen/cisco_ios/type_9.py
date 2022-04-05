import scrypt
import base64

from network_hash_gen.base import BaseHash


class Type9(BaseHash):
    salt_length = 14
    salt_chars = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    _std_b64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    _b64table = str.maketrans(_std_b64chars, salt_chars)

    @classmethod
    def hash_salted(cls, password: str, salt: str) -> str:
        """
        Calculates a Cisco IOS/IOS-XE Type 9 hash with the given password and salt.

        This function assumes that the given salt is valid for that hash.
        Using an invalid salt leads to undefined behaviour.
        Prefer the `type_9_hash` and `type_9_hash_seeded` functions over this one
        if possible.
        """

        hash = scrypt.hash(password, salt, 16384, 1, 1, 32)

        # Convert the hash from Standard Base64 to Cisco Base64
        hash = base64.b64encode(hash).decode().translate(cls._b64table)[:-1]

        return f"$9${salt}${hash}"
