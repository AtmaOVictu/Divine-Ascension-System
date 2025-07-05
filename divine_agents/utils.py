import math


def logistic_function(x: float, k: float = 1.0, c: float = 0.0) -> float:
    """Compute a logistic function value."""
    return 1.0 / (1.0 + math.exp(-k * (x - c)))
