from network_hash_gen.juniper_junos import Type6
from tests.hash_test_suite import BaseHashTest


class TestJuniperJunOSType1(BaseHashTest.HashTest):
    def setUp(self):
        self.group = Type6
        self.hash_password_pairs = [
            # ACX5448, JunOS 20.2R3-S2.5
            (
                "$6$R/EOMusB$JgxbO9XSJG/ElhaEZlXZHqwpGNqVgnEEKkpFpx3qJltjfB7dRBJUrhGNfPv43o/FPv6187SpmeRjClqbaN03f/",
                "0juniper0",
            ),
            (
                "$6$xuEGPTJ/$06se2Gr3s/eLY9ZF6AMVDR/ZIJ9g6mDuuDhFgujNw3JK.Q4bkU30OpNUFkYe/led3AaBsaV8JgQ2udOXsZzaG1",
                "1juniper1",
            ),
            (
                "$6$xV5M25yP$T8zhFshFyREifBJ5EQDnfiu.9XGqZE5Oezc2vR8zGTFbrkHVlwROAouTEq1aeGynGEwGG38.J0R.Q6xh1XkW.0",
                "2juniper2",
            ),
            (
                "$6$VXJBWHCV$TdcTDqbhR8aRkl07wjGAFwlBEPDxFuFxltQuxs0h6Fn6aeF6Ak/qhkwT63NZWtSQ9TsXiK06axoefwJG/YKZj0",
                "3juniper3",
            ),
            (
                "$6$BMl4hvqy$QFkm41ebEwlABgJ47pqmvOeAmPW4IMSUC3GwXAyzUVb21SrSajIuEnlvpoMcKvHBIyc5mcCi/L0ZFYWc6s.6Q/",
                "4juniper4",
            ),
            (
                "$6$phGs9WhT$9M/1Ki9lniHUQEEHfnePgGBg/pnSN4tROgRsCzQxHT/YXy.bS39xboiTGfxoCoXw3JrBhpCrT8FJxTEFxrIWP1",
                "5juniper5",
            ),
            (
                "$6$z7V8Xbla$oQgQ8Tt4a6RxStx5MgKmlx9ooh0.RiKyK7/WPedPE9edKCD4DGedENlzqNskKImQMAvezlvMUb0xsr3EfgvqZ1",
                "6juniper6",
            ),
            (
                "$6$XW.LadwP$6ToR0EkFvqR5jQia8kPVHsIqCQ3q8FlRHQBRjaSCsfLqKHDLvn8PY6DI0g8T5.nDXjN3CINAfJ0CfU8uIIH11/",
                "7juniper7",
            ),
            (
                "$6$zW3n3Fmd$O3xZxeVquFYeS2RNxdlaX06.PWOkQbjqiXCNwiHAHrRqhjDEqoaOoWA1vCSYvxIHfwY5q94It0r/3z8qmxzjB0",
                "8juniper8",
            ),
            (
                "$6$rV323yX5$0DlgBNrztj8YUxOIpPlcq/voleibdgO3RkvMI.KYJs/o2Vn4.Ees6QjGK4hqCaiZe8PyHu1Y64oZpN7OjxJAx1",
                "9juniper9",
            ),
        ]

        self.hash_password_seed_tuples = [
            (
                "$6$v4mca8NQ$QUVmP19Oxy61A44H8Zuah05nxnOSkQ0QC7fIm3MovsBqsKBMAUb21eLGBbb2idOPJWOMVcUlCNdD789vLGv9P0",
                "asdfasdfasdf",
                "tzuijhuikj",
            ),
            (
                "$6$UMmKKfUb$bxMa65Va7OkshQuPyDzoFFx8mBqDNHa9y9q1qTEGfbjzKtV0BuQkyGlWX01pczZZEqWDz63M8RWoG5Zy.PWBb0",
                "123sd()123!",
                "78/(123ksdiASDij",
            ),
        ]
