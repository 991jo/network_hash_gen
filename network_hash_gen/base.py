from typing import Optional
from abc import abstractmethod
from network_hash_gen.utils import _generate_salt as _generate


class BaseHash:
    """
    A base class that implements salt generation and the `hash` and
    `hash_seeded` functions.

    A subclass only needs to specify the `salt_length` and `salt_chars`
    methods and the `hash_salted` function.
    """

    salt_length: int
    """The length of the salt."""

    salt_chars: str
    """A string containing all characters that can be used in a salt."""

    @classmethod
    @abstractmethod
    def hash_salted(cls, password: str, salt: str) -> str:
        """
        calculates a hash from a fiven password and salt.
        If the salt is invalid for the hash, the behaviour is undefined.
        Prefer the `hash` and `hash_seeded` methods over this one if possible.
        """
        pass  # pragma: no cover

    @classmethod
    def _generate_salt(cls, seed: Optional[str] = None) -> str:
        """
        Generates a salt for the hash.

        If `seed` is specified the value is used to initialize the random number
        generator.
        """
        return _generate(cls.salt_chars, cls.salt_length, seed=seed)

    @classmethod
    def hash(cls, password: str) -> str:
        """
        Calculates the hash.

        An appropriate salt is chosen randomly.
        """
        salt = cls._generate_salt()
        return cls.hash_salted(password, salt)

    @classmethod
    def hash_seeded(cls, password: str, seed: str) -> str:
        """
        Calculates a hash with the given seed used for generating a appropriate
        salt.

        Use this function if you have to generate a password multiple times (e.g.
        when generating configs) to generate the same hash every time.
        """
        salt = cls._generate_salt(seed)
        return cls.hash_salted(password, salt)
