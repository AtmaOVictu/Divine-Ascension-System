"""Surreal ontological transition modeled with logistic functions."""

from typing import List, Sequence

import math


def logistic_function(t: float, k: float, c: float) -> float:
    """Compute logistic transition for a single phase."""
    return 1 / (1 + math.exp(-k * (t - c)))


def surreal_transition(t: float, k_values: Sequence[float], c_values: Sequence[float]) -> List[float]:
    """Return states after passing through nine surreal phases.

    Parameters
    ----------
    t: float
        Initial value in range [0, 1] representing potentiality.
    k_values: Sequence[float]
        Speed coefficients for each phase.
    c_values: Sequence[float]
        Critical points for each phase.

    Returns
    -------
    List[float]
        Values after each phase transformation.
    """
    if len(k_values) != 9 or len(c_values) != 9:
        raise ValueError("k_values and c_values must contain 9 elements")

    p = t
    states = []
    for k, c in zip(k_values, c_values):
        p = logistic_function(p, k, c)
        states.append(p)
    return states
