import math


def logistic(x: float, k: float = 1.0, x0: float = 0.5) -> float:
    """Basic logistic function used to smooth tension."""
    return 1 / (1 + math.exp(-k * (x - x0)))
