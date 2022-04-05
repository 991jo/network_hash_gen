from network_hash_gen.cisco_ios import Type5
from tests.hash_test_suite import BaseHashTest


class TestCisocIOSType5(BaseHashTest.HashTest):
    def setUp(self):
        self.group = Type5
        self.hash_password_pairs = [
            # ASR920, IOS-XE 16.09.05f
            ("$1$u5Qz$ASoUsdGV2sOmi8XYkTuex1", "0foo0"),
            ("$1$Awu/$1X3gez8VPPh9.McBXfA1..", "1foo1"),
            ("$1$7R0z$CUJUEZXE/CS0kHkyGWtcb/", "2foo2"),
            ("$1$WF3X$GaRbNTz64GhwYHG0PquQw/", "3foo3"),
            ("$1$8OAY$GAKB/Yfz3ua4JCHfUAoUo0", "4foo4"),
            ("$1$Z2yX$hTf/MOQQYpaRCCFMJ1Wo//", "5foo5"),
            ("$1$OA7L$25A2lP5L0xvdIUu.8asgx/", "6foo6"),
            ("$1$3.ND$cRS/.rSfCIlwGuW0H3YzW.", "7foo7"),
            ("$1$tVk7$JAnQZwfmGZBk4TslhclFY.", "8foo8"),
            ("$1$262O$Hyxgu5up0M6a7nbsUZXmu/", "9foo9"),
            # C9300, IOS-XE 16.09.05
            ("$1$FCLB$2a3ny5w.KvoBl9WtjJePx1", "0foo0"),
            ("$1$bR4d$TcOVI.MROLfU2Gh4aXQrb0", "1foo1"),
            ("$1$Hl7d$LvCxzKmSxvv0ueXHTF6FO/", "2foo2"),
            ("$1$nXcV$JZEq6Mq639ef1eAKWiOxS1", "3foo3"),
            ("$1$C1ji$9Tfj7L4m5gDr5U2mvjfWU1", "4foo4"),
            ("$1$rRaQ$GvbTY9nLhVDm7CjvS/1yM.", "5foo5"),
            ("$1$vkQG$623sdz.eF3/6ueT.yiwRl0", "6foo6"),
            ("$1$ebEh$Me78poVDb0tfYX//MuYsU/", "7foo7"),
            ("$1$ezpt$YNP.lTuCJFI/CSYtQuicz.", "8foo8"),
            ("$1$t0yF$gNSfdCyGLt5kWicAv7qgf0", "9foo9"),
        ]

        self.hash_password_seed_tuples = [
            ("$1$v4mc$2Suu.8oPyYRG0.XUfV75D0", "asdfasdfasdf", "tzuijhuikj"),
            ("$1$UMmK$dKZmb7om9b6O/E/qlRILM0", "123sd()123!", "78/(123ksdiASDij"),
        ]
