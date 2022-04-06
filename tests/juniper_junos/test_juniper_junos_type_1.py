from network_hash_gen.juniper_junos import Type1
from tests.hash_test_suite import BaseHashTest


class TestJuniperJunOSType1(BaseHashTest.HashTest):
    def setUp(self):
        self.group = Type1
        self.hash_password_pairs = [
            # EX2200, JunOS 12.3R12-S9
            ("$1$kXW66D.w$JQpS7wkzFxvP..77XQ.t./", "0juniper0"),
            ("$1$cfkJPjtt$aZvXKK7.5dI49kaRkqWdh/", "1juniper1"),
            ("$1$lPi5arXQ$WliarhLbx45LYy5M0kmvq1", "2juniper2"),
            ("$1$s4.yjibi$Pr3VMZoUVWFNN/eT2OYu/.", "3juniper3"),
            ("$1$dD8H5wL8$DjCJadySUEw0b.PPu59BV/", "4juniper4"),
            ("$1$ix8OLcAF$82wL/dbstKVplYcn42Xa8/", "5juniper5"),
            ("$1$P1eKIpfm$rCBByWMVExATuWRrBN1Hk0", "6juniper6"),
            ("$1$qkVyrI1v$3jCcDxD0zdSzn9nmebt0O.", "7juniper7"),
            ("$1$BGUKGxtQ$fM8LK5kucP4IZfz/Rzd1M0", "8juniper8"),
            ("$1$r2DRyKh7$WnOrUXK2M5kMGLm3uQ.a//", "9juniper9"),
        ]

        self.hash_password_seed_tuples = [
            ("$1$v4mca8NQ$6p/gzjbl7tSQHZux03an0.", "asdfasdfasdf", "tzuijhuikj"),
            ("$1$UMmKKfUb$SIQOrCfclFDJyRmGkVxr7.", "123sd()123!", "78/(123ksdiASDij"),
        ]
