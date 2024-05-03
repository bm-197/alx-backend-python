#!/usr/bin/env python3
"""A module for defining to_kv"""


def to_kv(k: str, v: int | float) -> tuple:
    """Make a tuple out of k and v"""
    return (k, float(v**2))
