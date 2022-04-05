from unittest import TestCase

from network_hash_gen.utils import _generate_salt


class TestGenerateSalt(TestCase):
    def test_single_char_salt(self):
        self.assertEqual("aaaa", _generate_salt("a", 4))
        self.assertEqual("aaaaaaaa", _generate_salt("a", 8))
        self.assertEqual("aaaa", _generate_salt("a", 4, "someseed"))

    def test_reproducible_salts(self):
        """
        This contains several precalculated salts to ensure that this function
        returns the same output in the future.
        """
        self.assertEqual("eefgfhgf", _generate_salt("abcdefgh", 8, seed="testseed"))
        self.assertEqual("ebgghhbh", _generate_salt("abcdefgh", 8, seed="testseed2"))
        self.assertEqual("ehcahbfh", _generate_salt("abcdefgh", 8, seed="testseed3"))
        self.assertEqual("ecbbfbbd", _generate_salt("abcdefgh", 8, seed="testseed4"))
