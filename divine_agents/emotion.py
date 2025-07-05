import math


def logistic_emotion(t: float, k: float = 1.0, c: float = 0.0) -> float:
    """Calculate emotion intensity using a logistic growth function.

    Parameters
    ----------
    t : float
        Time step or intensity value.
    k : float, optional
        Growth rate (default ``1.0``).
    c : float, optional
        Midpoint of the curve (default ``0.0``).

    Returns
    -------
    float
        Normalized emotion value between 0 and 1.
    """
    return 1 / (1 + math.exp(-k * (t - c)))
