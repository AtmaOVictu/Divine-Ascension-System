import math


def logistic_function(t: float, k: float = 1.0, c: float = 0.5) -> float:
    """Return the logistic growth value for time t."""
    return 1 / (1 + math.exp(-k * (t - c)))


def logarithmic_function(t: float, k: float = 1.0, c: float = 0.1) -> float:
    """Return the logarithmic value for time t, shifted by c."""
    return k * math.log(t + c)
