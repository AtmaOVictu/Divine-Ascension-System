import math


def logistic_function(t: float, k: float = 1.0, c: float = 0.5) -> float:
    """Simple logistic function used to modulate tension."""
    return 1 / (1 + math.exp(-k * (t - c)))
