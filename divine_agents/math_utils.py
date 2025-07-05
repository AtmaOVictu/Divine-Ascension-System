from math import exp, log


def logistic_function(t: float, k: float = 4.0, c: float = 0.5) -> float:
    """Return logistic curve value for given t."""
    return 1 / (1 + exp(-k * (t - c)))


def logarithmic_function(t: float, k: float = 1.0, c: float = 0.1) -> float:
    """Return logarithmic growth value for given t."""
    return k * log(t + c)
