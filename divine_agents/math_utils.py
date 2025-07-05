"""Mathematical helper functions for agent transitions."""

from __future__ import annotations

import math


def logistic_function(t: float, k: float, c: float) -> float:
    """Logistic function modeling rapid transition.

    Parameters
    ----------
    t : float
        Current value (e.g., time or tension).
    k : float
        Transition rate.
    c : float
        Critical point of transition.

    Returns
    -------
    float
        Value of the logistic function at ``t``.
    """
    return 1 / (1 + math.exp(-k * (t - c)))


def logarithmic_function(t: float, k: float, c: float) -> float:
    """Logarithmic growth function.

    Parameters
    ----------
    t : float
        Current value used in the growth calculation.
    k : float
        Growth coefficient.
    c : float
        Offset to ensure the argument to ``log`` is positive.

    Returns
    -------
    float
        Value of the logarithmic function at ``t``.
    """
    return k * math.log(t + c)

