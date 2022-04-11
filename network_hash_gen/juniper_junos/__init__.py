"""
This module provides hash functions for Juniper Junos


Supported are:

  - Type 1 (md5-based)
  - Type 6 (sha512-based)
  - Type 9 (Vigenère-based (not a secure hash, must a obfuscation))
"""
from .type_1 import Type1
from .type_6 import Type6
from .type_9 import Type9

__pdoc__ = {}

__all__ = ["Type1", "Type6", "Type9"]
