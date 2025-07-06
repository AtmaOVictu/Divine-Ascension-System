"""Utility helpers for agent state calculations."""

from __future__ import annotations


def numerological_value(value: float, scale: float = 1.0) -> float:
    """Return a numerological interpretation between 0 and 10."""
    if scale == 0:
        return 0.0
    result = (value / scale) * 10
    # Clamp result to 0-10 range and round for readability
    result = max(0.0, min(result, 10))
    return round(result, 2)

