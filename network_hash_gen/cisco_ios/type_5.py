from typing import ByteString, Optional
from passlib.hash import md5_crypt
import random

md5_crypt_salt_chars = (
    "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
)


def type_5_hash_salted(password: ByteString, salt: ByteString) -> ByteString:
    """
    Calculates a Cisco IOS/IOS-XE Type 5 hash with the given password and salt.
    """

    salt_str = bytes(salt).decode()
    m = md5_crypt.using(salt=salt_str).hash(password)
    return bytearray(m, encoding="utf-8")


def _generate_type_5_salt(seed: Optional[str] = None) -> ByteString:
    """
    Generates a salt for Cisco IOS type 5 hashes.

    If `seed` is specified the value is used to initialize the random number
    generator.
    """

    # initialize a seperate RNG to no seed the global instance used by the
    # functions called directly on the random module.
    rng = random.Random()

    if seed is not None:
        rng.seed(seed)

    output = ""
    for _ in range(4):
        output += rng.choice(md5_crypt_salt_chars)

    return bytearray(output, encoding="utf-8")


def type_5_hash_seeded(password: ByteString, seed: str) -> ByteString:
    """
    Calculates a Cisco IOS/IOS-XE Type 5 hash with the given seed used for
    generating a appropriate salt.

    Use this function if you have to generate a password multiple times (e.g.
    when generating configs) to generate the same hash every time.
    """
    salt = _generate_type_5_salt(seed)
    return type_5_hash_salted(password, salt)


def type_5_hash(password: ByteString) -> ByteString:
    """
    Calculates a Cisco IOS/IOS-XE Type 5 hash.

    An appropriate salt is chosen randomly.
    """
    salt = _generate_type_5_salt()
    return type_5_hash_salted(password, salt)
