"""
This module provides hash functions for Juniper Junos

Currently only type 1 (md5-based) and type 6 (SHA512-based) are supported.
"""
from .type_1 import Type1
from .type_6 import Type6

__pdoc__ = {}

__all__ = ["Type1", "Type6"]
