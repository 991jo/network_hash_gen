from passlib.hash import md5_crypt
from network_hash_gen.base import BaseHash


class Type5(BaseHash):
    """
    Calculates the md5-crypt based type 5 hashes for Cisco IOS/IOS-XE.
    """

    salt_chars = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    salt_length = 4

    @classmethod
    def hash_salted(cls, password: str, salt: str) -> str:
        """
        Calculates a Cisco IOS/IOS-XE Type 5 hash with the given password and
        salt.

        This function assumes that the given salt is valid for that hash.
        Using an invalid salt leads to undefined behaviour.
        Prefer the `hash` and `hash_seeded` functions over this
        one if possible.
        """

        m = md5_crypt.using(salt=salt).hash(password)
        return m
