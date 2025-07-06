"""Utility functions for numerical scaling and other helpers."""

from typing import Union


def numerological_value(value: Union[int, float], scale: Union[int, float] = 10) -> float:
    """Return a numerological interpretation between 0 and 10."""
    return round((value / scale) * 10, 2)
