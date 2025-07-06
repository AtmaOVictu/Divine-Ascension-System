import math


def calculate_log(value: float, base: float = 10) -> float:
    """Calculate logarithm of a value with specified base."""
    if value <= 0:
        raise ValueError("Value must be positive")
    if base <= 0 or base == 1:
        raise ValueError("Base must be positive and not equal to 1")
    return math.log(value, base)
