#!/usr/bin/env python3
"""A module to modify the given function"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Finds the length of each element"""
    return [(i, len(i)) for i in lst]
