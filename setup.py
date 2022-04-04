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
    install_requires=["passlib == 1.7.4", "scrypt == 0.8.20"],
    extras_require={"dev": ["black"], "docs": ["pdoc3"]},
)
