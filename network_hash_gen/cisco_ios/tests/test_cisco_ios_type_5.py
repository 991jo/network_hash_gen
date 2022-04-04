from unittest import TestCase

from ..type_5 import type_5_hash_salted


class TestCiscoIOSType5(TestCase):
    def test_salted(self):

        # hash, plaintext
        data = [
            # ASR920, IOS-XE 16.09.05f
            (b"$1$u5Qz$ASoUsdGV2sOmi8XYkTuex1", b"0foo0"),
            (b"$1$Awu/$1X3gez8VPPh9.McBXfA1..", b"1foo1"),
            (b"$1$7R0z$CUJUEZXE/CS0kHkyGWtcb/", b"2foo2"),
            (b"$1$WF3X$GaRbNTz64GhwYHG0PquQw/", b"3foo3"),
            (b"$1$8OAY$GAKB/Yfz3ua4JCHfUAoUo0", b"4foo4"),
            (b"$1$Z2yX$hTf/MOQQYpaRCCFMJ1Wo//", b"5foo5"),
            (b"$1$OA7L$25A2lP5L0xvdIUu.8asgx/", b"6foo6"),
            (b"$1$3.ND$cRS/.rSfCIlwGuW0H3YzW.", b"7foo7"),
            (b"$1$tVk7$JAnQZwfmGZBk4TslhclFY.", b"8foo8"),
            (b"$1$262O$Hyxgu5up0M6a7nbsUZXmu/", b"9foo9"),
            # C9300, IOS-XE 16.09.05
            (b"$1$FCLB$2a3ny5w.KvoBl9WtjJePx1", b"0foo0"),
            (b"$1$bR4d$TcOVI.MROLfU2Gh4aXQrb0", b"1foo1"),
            (b"$1$Hl7d$LvCxzKmSxvv0ueXHTF6FO/", b"2foo2"),
            (b"$1$nXcV$JZEq6Mq639ef1eAKWiOxS1", b"3foo3"),
            (b"$1$C1ji$9Tfj7L4m5gDr5U2mvjfWU1", b"4foo4"),
            (b"$1$rRaQ$GvbTY9nLhVDm7CjvS/1yM.", b"5foo5"),
            (b"$1$vkQG$623sdz.eF3/6ueT.yiwRl0", b"6foo6"),
            (b"$1$ebEh$Me78poVDb0tfYX//MuYsU/", b"7foo7"),
            (b"$1$ezpt$YNP.lTuCJFI/CSYtQuicz.", b"8foo8"),
            (b"$1$t0yF$gNSfdCyGLt5kWicAv7qgf0", b"9foo9"),
        ]

        for hash, plaintext in data:
            salt = hash.split(b"$")[2]
            self.assertEqual(hash, type_5_hash_salted(plaintext, salt))
