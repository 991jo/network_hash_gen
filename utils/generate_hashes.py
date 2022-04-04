from network_hash_gen.cisco_ios.type_9 import type_9_hash_seeded

for i in range(10):
    password = f"foo{i}"
    hash = type_9_hash_seeded(password, f"some_seed{i}")
    print(f"username test{i} secret 9 { hash }")
