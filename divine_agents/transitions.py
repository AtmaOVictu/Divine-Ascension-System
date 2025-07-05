"""Transition helpers based on logistic curves."""

import math


def logistic(t: float, k: float, c: float) -> float:
    """General logistic function used for transitions."""
    return 1.0 / (1.0 + math.exp(-k * (t - c)))


def biological_transition(t: float, k_bio: float, c_bio: float) -> float:
    """Logistic curve representing biological transition intensity."""
    return logistic(t, k_bio, c_bio)


def social_transition(t: float, k_soc: float, c_soc: float) -> float:
    """Logistic curve representing social transition intensity."""
    return logistic(t, k_soc, c_soc)
