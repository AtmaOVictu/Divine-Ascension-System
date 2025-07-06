"""Utility functions for numerological interpretations of agent values."""

def numerological_value(value: float, scale: float = 10) -> float:
    """Return a value normalized on a 0-10 scale for numerological use."""
    if scale == 0:
        raise ValueError("Scale must be non-zero")
    return round((value / scale) * 10, 2)

