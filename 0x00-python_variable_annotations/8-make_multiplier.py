#!/usr/bin/env python3
"""A module defining make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> float:
    """Creates multiplier function"""
    return lambda x: x * multiplier
