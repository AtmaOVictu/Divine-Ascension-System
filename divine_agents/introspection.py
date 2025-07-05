import math


def exponential_introspection(t: float, k: float) -> float:
    """Calculate exponential introspection level."""
    return math.exp(k * t)


def phenomenological_contraction(t: float, k: float) -> float:
    """Represent contraction of awareness over time."""
    return math.exp(-k * t)


def extractive_introspection(t: float, k: float) -> float:
    """Extract essential insight over time using integral of the exponential."""
    if k == 0:
        return t
    return (math.exp(k * t) - 1) / k
