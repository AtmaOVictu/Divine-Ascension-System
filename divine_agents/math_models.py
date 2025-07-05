"""Mathematical helper functions for ontological transitions."""

import math
from typing import Iterable, List


def logistic_function(t: float, k: float, c: float) -> float:
    """Return logistic growth value at time ``t``."""
    return 1 / (1 + math.exp(-k * (t - c)))


def logarithmic_function(t: float, k: float, c: float) -> float:
    """Return logarithmic growth value at time ``t``."""
    return k * math.log(t + c)


def generate_sequence(func, times: Iterable[float], *args: float) -> List[float]:
    """Helper to produce a list of values from ``func`` over ``times``."""
    return [func(t, *args) for t in times]
