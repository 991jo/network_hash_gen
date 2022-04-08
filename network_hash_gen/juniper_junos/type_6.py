from passlib.hash import sha512_crypt

from network_hash_gen.base import BaseHash


class Type6(BaseHash):
    """
    SHA2 512 bit based hash for Juniper JunOS.

    Specification: https://akkadia.org/drepper/SHA-crypt.txt
    Details:
    - 5000 rounds are used
    - the round specifier is omitted.
    """

    salt_length = 8
    salt_chars = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    @staticmethod
    def hash_salted(password: str, salt: str) -> str:
        return sha512_crypt.using(salt=salt, rounds=5000).hash(password)
