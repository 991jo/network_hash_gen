from crypt import crypt

from network_hash_gen.base import BaseHash


class Type6(BaseHash):

    salt_length = 8
    salt_chars = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    @staticmethod
    def hash_salted(password: str, salt: str) -> str:
        return crypt(password, f"$6${salt}")
