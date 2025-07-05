import math


def logistic_growth(t: float, k: float = 1.0, c: float = 0.5) -> float:
    """Return logistic growth value for time `t`."""
    return 1 / (1 + math.exp(-k * (t - c)))


def logarithmic_progress(t: float, k: float = 1.0, c: float = 0.1) -> float:
    """Return logarithmic progression value for time `t`."""
    return k * math.log(t + c)
