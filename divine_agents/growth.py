import math


def logistic_growth(t, k=1.0, c=0.5):
    """Return the logistic growth value for time ``t``.

    Parameters
    ----------
    t : float or array-like
        Time step(s) at which to evaluate the function.
    k : float, optional
        Growth rate. Default is 1.0.
    c : float, optional
        Midpoint of the curve. Default is 0.5.
    """
    return 1 / (1 + math.exp(-k * (t - c)))

