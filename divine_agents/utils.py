"""Utility functions for the Divine Ascension system."""
from __future__ import annotations

import math


def logistic_function(t: float, k: float = 1.0, c: float = 0.5) -> float:
    """Return logistic growth value for ``t``.

    Parameters
    ----------
    t:
        Input value.
    k:
        Growth rate.
    c:
        Midpoint of the transition.
    """
    return 1 / (1 + math.exp(-k * (t - c)))
