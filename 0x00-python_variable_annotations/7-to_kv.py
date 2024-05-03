#!/usr/bin/env python3
"""A module for defining to_kv"""
from typing import Tuple, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Make a tuple out of k and v"""
    return (k, float(v**2))
