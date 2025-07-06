"""Numerological utilities for normalizing agent values."""

from typing import Union


def numerological_value(value: Union[int, float], scale: Union[int, float] = 1.0) -> float:
    """Return a value normalized to a 0-10 numerological scale."""
    if scale == 0:
        raise ValueError("scale must be non-zero")
    normalized = (value / scale) * 10
    return round(normalized, 2)
