from setuptools import setup, find_packages
from network_hash_gen import __version__

with open("README.md") as f:
    readme = f.read()

setup(
    name="network_hash_gen",
    version=__version__,
    packages=find_packages(),
    url="",
    author="Johannes Erwerle",
    author_email="jo+network_hash_gen@swagspace.org",
    description="A library to generate hashes for network devices.",
    long_description=readme,
    extras_require={"dev": ["black"]},
)
