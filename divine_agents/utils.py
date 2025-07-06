"""Utility functions for Divine-Ascension agents."""


def numerological_value(value: float, scale: float = 1.0) -> float:
    """Return a numerological value on a 0-10 scale."""
    if scale == 0:
        raise ValueError("Scale must be non-zero")
    return round((value / scale) * 10, 2)


