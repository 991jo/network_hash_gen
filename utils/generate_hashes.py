from network_hash_gen.cisco_ios import Type9

for i in range(10):
    password = f"foo{i}"
    hash = Type9.hash_seeded(password, f"some_seed{i}")
    print(f"username test{i} secret 9 { hash }")
