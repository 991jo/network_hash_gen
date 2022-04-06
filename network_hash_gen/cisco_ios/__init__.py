"""
This module provides hash functions for Cisco IOS and IOS-XE.

Currently only type 5 (md5-based) and type 9 (scrypt-based) are supported.
"""
from .type_5 import Type5
from .type_9 import Type9

__all__ = ["Type5", "Type9"]
