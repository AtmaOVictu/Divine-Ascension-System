"""Utility functions for numerological calculations."""

from typing import Union


def numerological_value(value: Union[int, float], scale: float = 10.0) -> float:
    """Return value normalized to a 0-10 scale rounded to two decimals."""
    if scale == 0:
        raise ValueError("scale must be non-zero")
    return round((value / scale) * 10, 2)
