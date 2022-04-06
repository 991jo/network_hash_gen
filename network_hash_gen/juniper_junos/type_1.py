from network_hash_gen.cisco_ios import Type5 as CiscoType5


class Type1(CiscoType5):
    """
    Calculates the md5-crypt based type 1 hashes for Juniper Junos.
    """

    salt_length = 8
