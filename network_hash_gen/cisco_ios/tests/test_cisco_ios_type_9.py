from unittest import TestCase

from ..type_9 import type_9_hash_salted


class TestCiscoIOSType5(TestCase):
    def test_salted(self):

        # hash, plaintext
        data = [
            # ASR920, IOS-XE 16.09.05f
            (
                b"$9$plz/kf0e3.dns.$cKvJDd6bXmyaUWdx42dgcRwpdDs0djBEqzjlmMbYEW6",
                b"0foo0",
            ),
            (
                b"$9$8Yn1IbhUG.YOGk$B0Tce.G3lMqSLb.qhSwQwxyi4qBU3jSlH2qTIelK.A2",
                b"1foo1",
            ),
            (
                b"$9$PMqVmgmR4Nvlsk$JzTbAxkZuDpMGImpXHGysj6uWjcQnikXR0GBdUhmdxw",
                b"2foo2",
            ),
            (
                b"$9$iMKNK2MyDfqPsU$V443Y/yutR./oArWmQA7pj6BNp5TrgC0MmGZ7VIKff2",
                b"3foo3",
            ),
            (
                b"$9$MigKM5HW.PsFlU$nUUsOfUnGck.G6q.9j0gqlb4vXDQIihOlkYaFuQ0/0g",
                b"4foo4",
            ),
            (
                b"$9$5vByDSrtKlVj8.$RhjgPmH7GTJpjbb3brYqQOXtP.UIpMiqS644VA.N12A",
                b"5foo5",
            ),
            (
                b"$9$3ayas1CG7gPWd.$FF2Y5kel8EIjGlJTjw0kBu3GLtk2RIWIaO2Uiq3Q8vs",
                b"6foo6",
            ),
            (
                b"$9$02NxZc3g6VBz4U$OC9gBCsRyES802CP/A5DwFx1uAQt/rs2FQh7D6t9h/E",
                b"7foo7",
            ),
            (
                b"$9$mK1ofpcD0RU9ek$YMRifOqC95igMZnew84jvZfpjg9Ux68ez3L2Z0av8g2",
                b"8foo8",
            ),
            (
                b"$9$gSxJfegHuj0F6E$ENXdRsApTMICSTVFZcTWlNpYqcmWSEwcqsklANu6vb2",
                b"9foo9",
            ),
            # C9300, IOS-XE 16.09.05
            (
                b"$9$PXg4rSaFnoegO1$/6Rz3Wj5QFPep7vO1ZucuQX5m34V4riND55WJabgpPI",
                b"0foo0",
            ),
            (
                b"$9$WtRdvMXgJ.ucTH$aLBq6tLlZ5wQkaENKWNRVjj8lBcegs1NnMuT0ePzckE",
                b"1foo1",
            ),
            (
                b"$9$0pjeJLxng3RwIn$pVvqIza/0yx7OxwtPuxPnVo7zynzIF6KIfUqwSWLJks",
                b"2foo2",
            ),
            (
                b"$9$3Y/3AuJhoMgzW1$2cGvk9ttc0KDz4IpNwUBVLyl.SkXSOMirLvEnRRE0Qg",
                b"3foo3",
            ),
            (
                b"$9$Pm74lahwSPCK41$paN5FRwrc5IvjIDvqpfFoW8xeVmlBLi8OgAQWUX/6N2",
                b"4foo4",
            ),
            (
                b"$9$L83ULmQYYBEhbn$X0E3XEAlNJSuj1ONaVRy.45vrcR9fPudODlJWd3XSBo",
                b"5foo5",
            ),
            (
                b"$9$kdO8GOTC5on42X$Hvkr53ivGpUPHcoFOBXzB9I/E0ccFeOoBzdqjXBiBSI",
                b"6foo6",
            ),
            (
                b"$9$dSnrddpzAU9uhH$cMALHjMkiDsBztHRSPjZC0S0WyNYnC5nRHGQHtCVDGg",
                b"7foo7",
            ),
            (
                b"$9$dynV4r5F4XwFdH$yuN0E1i14DhOb04xilIp1lJ.N/IKJakDylS/EvMTc6w",
                b"8foo8",
            ),
            (
                b"$9$dddcyrMXj2f4tX$5wDEL2q.fmZRUP47ZlB9NpvMEgWwjtxMdYnhUH7kOmk",
                b"9foo9",
            ),
        ]

        for hash, plaintext in data:
            salt = hash.split(b"$")[2]
            self.assertEqual(hash, type_9_hash_salted(plaintext, salt))
