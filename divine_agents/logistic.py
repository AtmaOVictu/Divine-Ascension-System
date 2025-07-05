import math


def logistic_transition(x: float, k: float = 5.0, c: float = 0.5) -> float:
    """Return logistic value for transition intensity."""
    return 1 / (1 + math.exp(-k * (x - c)))
