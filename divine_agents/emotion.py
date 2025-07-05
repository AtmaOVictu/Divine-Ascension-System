import math
from typing import Sequence, List


def logistic(t: float, k: float, c: float) -> float:
    """Compute logistic emotion intensity.

    Parameters
    ----------
    t : float
        Time or intensity parameter.
    k : float
        Growth rate controlling transition speed.
    c : float
        Critical point when emotion rapidly increases.
    Returns
    -------
    float
        Emotion intensity between 0 and 1.
    """
    return 1 / (1 + math.exp(-k * (t - c)))


def emotion_series(time_steps: Sequence[float], k: float, c: float) -> List[float]:
    """Generate a series of emotion values across time steps."""
    return [logistic(t, k, c) for t in time_steps]
