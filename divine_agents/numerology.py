"""Utility functions for numerological interpretations."""


def numerological_value(value: float, scale: float = 10) -> float:
    """Return a numerological interpretation between 0 and 10."""
    return round((value / scale) * 10, 2)
