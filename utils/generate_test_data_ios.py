# This script prints some test commands.

for i in range(10):
    print(f"username test{i} secret {i}foo{i}")

for i in range(10):
    print(f"username test{i} algorithm-type scrypt secret {i}foo{i}")

print("do-exec show run | incl username test")

for i in range(10):
    print(f"no username test{i}")
