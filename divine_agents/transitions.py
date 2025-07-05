import math


def biological_transition(t: float, k_bio: float = 1.0, c_bio: float = 0.5) -> float:
    """Compute biological transition intensity using a logistic function."""
    return 1 / (1 + math.exp(-k_bio * (t - c_bio)))


def social_transition(t: float, k_soc: float = 1.5, c_soc: float = 0.6) -> float:
    """Compute social transition intensity using a logistic function."""
    return 1 / (1 + math.exp(-k_soc * (t - c_soc)))
