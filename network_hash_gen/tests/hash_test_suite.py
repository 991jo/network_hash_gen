from unittest import TestCase


class BaseHashTest:
    class HashTest(TestCase):
        """
        This class runs several tests for a group of function belonging to a hash
        scheme.

        This group is expected to be a class having the following classmethods:
        - `hash`
        - `hash_salted`
        - `hash_seeded`
        - `_generate_salt`

        This class has the following instance variables, which need to be set:

        - `group`: the class representing the hash scheme
        - `hash_password_pairs: List(Tuple(str, str))` A list of hash and password pairs.
          They are used to test whether the salted hash version returns the correct
          hashes. The hashes here are usually taken from device configs.
        - `hash_password_seed_tuples: List(Tuple(str, str, str))` A list of hashes,
          passwords and seeds. This is used to ensure that the seeded version of the
          hash returns the same values in the future.
        """

        def test_hash_pairs(self):

            assert getattr(self, "group") is not None
            assert getattr(self, "hash_password_pairs") is not None

            assert len(self.hash_password_pairs) > 0

            for hash, plaintext in self.hash_password_pairs:
                salt = hash.split("$")[2]
                self.assertEqual(hash, self.group.hash_salted(plaintext, salt))

        def test_hash_password_seed_tuples(self):

            assert getattr(self, "group") is not None
            assert getattr(self, "hash_password_seed_tuples") is not None

            assert len(self.hash_password_seed_tuples) > 0

            for hash, password, seed in self.hash_password_seed_tuples:
                self.assertEqual(hash, self.group.hash_seeded(password, seed))
