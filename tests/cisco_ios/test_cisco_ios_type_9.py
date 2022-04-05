from tests.hash_test_suite import BaseHashTest
from network_hash_gen.cisco_ios import Type9


class TestCiscoIOSType9(BaseHashTest.HashTest):
    def setUp(self):
        self.group = Type9
        self.hash_password_pairs = [
            # ASR920, IOS-XE 16.09.05f
            (
                "$9$plz/kf0e3.dns.$cKvJDd6bXmyaUWdx42dgcRwpdDs0djBEqzjlmMbYEW6",
                "0foo0",
            ),
            (
                "$9$8Yn1IbhUG.YOGk$B0Tce.G3lMqSLb.qhSwQwxyi4qBU3jSlH2qTIelK.A2",
                "1foo1",
            ),
            (
                "$9$PMqVmgmR4Nvlsk$JzTbAxkZuDpMGImpXHGysj6uWjcQnikXR0GBdUhmdxw",
                "2foo2",
            ),
            (
                "$9$iMKNK2MyDfqPsU$V443Y/yutR./oArWmQA7pj6BNp5TrgC0MmGZ7VIKff2",
                "3foo3",
            ),
            (
                "$9$MigKM5HW.PsFlU$nUUsOfUnGck.G6q.9j0gqlb4vXDQIihOlkYaFuQ0/0g",
                "4foo4",
            ),
            (
                "$9$5vByDSrtKlVj8.$RhjgPmH7GTJpjbb3brYqQOXtP.UIpMiqS644VA.N12A",
                "5foo5",
            ),
            (
                "$9$3ayas1CG7gPWd.$FF2Y5kel8EIjGlJTjw0kBu3GLtk2RIWIaO2Uiq3Q8vs",
                "6foo6",
            ),
            (
                "$9$02NxZc3g6VBz4U$OC9gBCsRyES802CP/A5DwFx1uAQt/rs2FQh7D6t9h/E",
                "7foo7",
            ),
            (
                "$9$mK1ofpcD0RU9ek$YMRifOqC95igMZnew84jvZfpjg9Ux68ez3L2Z0av8g2",
                "8foo8",
            ),
            (
                "$9$gSxJfegHuj0F6E$ENXdRsApTMICSTVFZcTWlNpYqcmWSEwcqsklANu6vb2",
                "9foo9",
            ),
            # C9300, IOS-XE 16.09.05
            (
                "$9$PXg4rSaFnoegO1$/6Rz3Wj5QFPep7vO1ZucuQX5m34V4riND55WJabgpPI",
                "0foo0",
            ),
            (
                "$9$WtRdvMXgJ.ucTH$aLBq6tLlZ5wQkaENKWNRVjj8lBcegs1NnMuT0ePzckE",
                "1foo1",
            ),
            (
                "$9$0pjeJLxng3RwIn$pVvqIza/0yx7OxwtPuxPnVo7zynzIF6KIfUqwSWLJks",
                "2foo2",
            ),
            (
                "$9$3Y/3AuJhoMgzW1$2cGvk9ttc0KDz4IpNwUBVLyl.SkXSOMirLvEnRRE0Qg",
                "3foo3",
            ),
            (
                "$9$Pm74lahwSPCK41$paN5FRwrc5IvjIDvqpfFoW8xeVmlBLi8OgAQWUX/6N2",
                "4foo4",
            ),
            (
                "$9$L83ULmQYYBEhbn$X0E3XEAlNJSuj1ONaVRy.45vrcR9fPudODlJWd3XSBo",
                "5foo5",
            ),
            (
                "$9$kdO8GOTC5on42X$Hvkr53ivGpUPHcoFOBXzB9I/E0ccFeOoBzdqjXBiBSI",
                "6foo6",
            ),
            (
                "$9$dSnrddpzAU9uhH$cMALHjMkiDsBztHRSPjZC0S0WyNYnC5nRHGQHtCVDGg",
                "7foo7",
            ),
            (
                "$9$dynV4r5F4XwFdH$yuN0E1i14DhOb04xilIp1lJ.N/IKJakDylS/EvMTc6w",
                "8foo8",
            ),
            (
                "$9$dddcyrMXj2f4tX$5wDEL2q.fmZRUP47ZlB9NpvMEgWwjtxMdYnhUH7kOmk",
                "9foo9",
            ),
        ]
        self.hash_password_seed_tuples = [
            (
                "$9$5A/0NQGf6wMdjN$4toTqNCPcBmsBgUsOxNy6uPLITQ4zKFfcf5sJuy3uMo",
                "asdfgsasdf",
                "asdfasdfasdfas",
            )
        ]
