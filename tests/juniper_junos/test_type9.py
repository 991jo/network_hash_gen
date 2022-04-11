from typing import List
from unittest import TestCase

from network_hash_gen.juniper_junos.type_9 import Type9


class TestJuniperJunOSType9(TestCase):
    def setUp(self):
        self.encoding_plaintext_pairs: List[str, str] = [
            ("$9$wysoJmPQ/A0mf9pu0cSvWL7b2goJ", "0juniper0"),
            ("$9$7mNwYji.Q39jHz6/9B1SreMxdVwY", "0juniper0"),
            ("$9$lsOe8X2gJiqf24HmPf6/uO1ErvM8X", "0juniper0"),
            ("$9$9gKsC0BeK8-b2evdsY2UD.P5z/tp0B", "0juniper0"),
            ("$9$M5hW7-aJD.fzaZmTQzAt1RhyvLX7-", "0juniper0"),
            ("$9$DFiHm", "a"),
            ("$9$TF39tpB", "bb"),
            ("$9$T3nCu0IcSe", "ccc"),
            ("$9$-zdb2JZj.mTNd", "dddd"),
            ("$9$QRTdFnCOBEleW36pB", "eeeee"),
            ("$9$4eJGif5FAtODifzn/0O", "ffffff"),
            ("$9$4rZUHTQnu0Ik.F/tuEhvWL", "ggggggg"),
            ("$9$oCaGiTQn69pUj5F3/0OylKv87", "hhhhhhhh"),
            ("$9$3qeg6CuSyKM87uOrvWXbwGDikmTAtO", "iiiiiiiii"),
            ("$9$VNsgJmPQ36AUjQn9tIRM8XNVYji.fT3", "jjjjjjjjjj"),
            ("$9$FbQF/A0leWxNbEcX-w2GUTz39tOeK87-whS", "kkkkkkkkkkk"),
            ("$9$UODkPAtOEcl69hrlMN-ZUji.5pu1cyK9ASe", "llllllllllll"),
            ("$9$MaH87VDjqTz6GDF/CuEhxNdb2af5FCtOmfpBIcvM", "mmmmmmmmmmmmm"),
        ]

    def test_encode(self):

        for test_encoded, plaintext in self.encoding_plaintext_pairs:
            test_salt, _, test_crypt = Type9._parse_encoding(test_encoded)

            encoded = Type9.encode_salted(plaintext, test_salt)
            enc_salt, _, enc_crypt = Type9._parse_encoding(encoded)

            self.assertEqual(enc_salt, test_salt)
            self.assertEqual(enc_crypt, test_crypt)

    def test_decode(self):

        for encoded, plaintext in self.encoding_plaintext_pairs:
            decoded = Type9.decode(encoded)
            self.assertEqual(decoded, plaintext)

    def test_encode_decode(self):
        """
        Tests whether things that are encoded are decoded correctly.
        """

        plaintexts = ["asdf", "oiajsdl223092" "test1", ""]

        for plaintext in plaintexts:
            encoded = Type9.encode(plaintext)
            self.assertEqual(plaintext, Type9.decode(encoded))

    def test_parse_encoding(self):

        self.assertEqual(Type9._parse_encoding("$9$wyasd"), (("w", "y", "asd")))
        self.assertEqual(
            Type9._parse_encoding("$9$Qabcqwertz"), (("Q", "abc", "qwertz"))
        )

    def test_encode_salted(self):

        self.assertEqual("$9$qmPQF39AtOaZUH", Type9.encode_seeded("aaaaa", "foo"))
        self.assertEqual("$9$JQUDkmPQ3nCYgaU", Type9.encode_seeded("bbbbb", "bar"))
