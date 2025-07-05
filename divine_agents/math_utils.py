import math


def logistic_function(t: float, k: float, c: float) -> float:
    """Return logistic growth result for given time and parameters."""
    return 1 / (1 + math.exp(-k * (t - c)))


def logarithmic_function(t: float, k: float, c: float) -> float:
    """Return logarithmic growth for given time and parameters."""
    return k * math.log(t + c)
