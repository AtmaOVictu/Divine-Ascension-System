"""Mathematical helpers for modelling agent progression."""
import math


def logistic_function(t: float, k: float, c: float) -> float:
    """Return logistic growth value at time ``t``.

    Parameters
    ----------
    t : float
        Time step.
    k : float
        Growth rate.
    c : float
        Midpoint of the curve.
    """
    return 1 / (1 + math.exp(-k * (t - c)))


def logarithmic_function(t: float, k: float, c: float) -> float:
    """Return logarithmic value for ``t`` ensuring positivity."""
    return k * math.log(t + c)
