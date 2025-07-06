"""Ontology utilities implementing validation, opposition and invalidation."""

from __future__ import annotations


def validate(x: float, exponent: float = 2.0) -> float:
    """Return x raised to a power representing validation."""
    return x ** exponent


def oppose(x: float) -> float:
    """Return the opposing value via division."""
    return 1 / x if x != 0 else float('inf')


def invalidate(x: float) -> float:
    """Return the inverse representing invalidation."""
    return x ** -1 if x != 0 else float('inf')
