# Network Hash Gen

Generating hashes for network devices like routers and switches - with the
option to specify seeds or salts.

# Currently supported hashes:

- Cisco IOS/IOS-XE
  - Type 5
  - Type 9

If you are missing a hash function, please open an issue.

# Example

This example generates a hash with a random salt and a hash with a given seed.
The first function returns a different hash most of the times while the
second one always returns the same hash value.

``` python3
>>> from network_hash_gen.cisco_ios import Type9
>>> Type9.hash("foobar")
'$9$FteIXKc69u9886$JFenYTrYz7kgex.60fbd8kzIg3Y/fE8lhsrtZeiif8k'
>>> Type9.hash_seeded("foobar", "$hostname-$username")
'$9$XpsDCh72ruxTQc$Cm80vIgCAQPhWrLJczX53Z7qVg0AxKui6t8.QbWfBsU'
```

# Documentation

The documentation build against the current master branch can be found here:
https://991jo.github.io/network_hash_gen

To build the documentation for a specific version run

```
pdoc3 --html --template-dir=templates network_hash_gen
```

This will generate documentation in a folder called `html`.

# Development

## Running the tests

The tests can be run with

```
python3 -m unittest discover
```

The unittests are also run via the pre-commit hooks.

To get test coverage reports [coverage](https://coverage.readthedocs.io/en/latest/)
is used. Run 

```
coverage run -m unittest discover
```

to run the tests and `coverage report` for a CLI report of `coverage html` to
generate a HTML version of the coverage report.

## Code Formatting

The code in this repository is formated with [black](https://github.com/psf/black).
The default settings are used.
Please format the code with black before commiting.
This can be done with

```
black network_hash_gen/
```

The code formatting is also checked (but not executed) in the commit hooks.

## Pre-Commit Hooks

There are pre-commit hooks that check the code formating and run the unittests.
To activate them, link the script in `scripts/pre-commit.sh` into your git hooks
directory:

```
cd .git/hooks/
ln -s ../../scripts/pre-commit
```
