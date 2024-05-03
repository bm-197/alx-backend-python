#!/usr/bin/env python3
"""A module for defining sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[str, float]]) -> float:
    """Calculates the total sum"""
    return float(sum(mxd_list))
