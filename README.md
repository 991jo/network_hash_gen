# Network Hash Gen

Generating hashes for network devices like routers and switches

# Currently supported hashes:

- Cisco IOS/IOS-XE
  - Type 5
  - Type 9

If you are missing a hash function, please open an issue.

# Documentation

The documentation build against the current master branch can be found here:
https://991jo.github.io/network_hash_gen

To build the documentation for a specific version run

```
pdoc3 --html network_hash_gen
```

This will generate documentation in a folder called `html`.

# Development

## Running the tests

The tests can be run with

```
python3 -m unittest discover
```

## Code Formatting.

The code in this repository is formated via [black](https://github.com/psf/black).
The default settings are used.
Please format the code with black before commiting.
This can be done with

```
black network_hash_gen/
```

The code formatting is also checked (but not executed) in the commit hooks.

## Pre-Commit Hooks

There are pre-commit hooks that run the code formating.
To activate them, link the script in `scripts/pre-commit.sh` into your git hooks
directory:

```
cd .git/hooks/
ln -s ../../scripts/pre-commit
```
