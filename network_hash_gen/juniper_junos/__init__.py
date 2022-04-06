"""
This module provides hash functions for Juniper Junos

Currently only type 1 (md5-based) is supported.
"""
from .type_1 import Type1

__pdoc__ = {}

__all__ = [
    "Type1",
]
