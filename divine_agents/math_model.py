"""Mathematical utilities for agent transitions."""

T_MAX = 1.0
E_MAX = 1.0
I_MAX = 1.0
O_MAX = 1.0


def transition_score(tension: float, emotion: float, interactions: float = 0.0, environment: float = 0.0) -> float:
    """Calculate the aggregated transition score."""
    return (tension / T_MAX + emotion / E_MAX + interactions / I_MAX + environment / O_MAX)


def transition_allowed(score: float, alpha: float = 1.5) -> bool:
    """Determine if transition is permitted based on score and threshold."""
    return score > alpha


def error_value(score: float, alpha: float = 1.5) -> float:
    """Return absolute difference between score and threshold."""
    return abs(score - alpha)
