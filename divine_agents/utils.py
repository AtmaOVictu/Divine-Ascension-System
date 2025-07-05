import math


def logistic_function(t: float, k: float = 10.0, c: float = 0.5) -> float:
    """Calculate logistic function for given value.

    Args:
        t: Input value representing time or tension.
        k: Steepness of the curve.
        c: Critical point where transition becomes noticeable.

    Returns:
        Normalized logistic value between 0 and 1.
    """
    return 1 / (1 + math.exp(-k * (t - c)))

