import math
from typing import Iterable, List

DEFAULT_K_VALUES = [0.5, 0.6, 0.7, 0.8, 1.0, 1.1, 1.2, 1.3, 1.5]
DEFAULT_C_VALUES = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]

def logistic_function(t: float, k: float, c: float) -> float:
    """Return logistic transform of ``t`` using parameters ``k`` and ``c``."""
    return 1.0 / (1.0 + math.exp(-k * (t - c)))

def surreal_transition(t: float,
                      k_values: Iterable[float] = DEFAULT_K_VALUES,
                      c_values: Iterable[float] = DEFAULT_C_VALUES) -> List[float]:
    """Calculate surreal transitions through nine phases.

    Parameters
    ----------
    t : float
        Initial value representing potentiality in range [0, 1].
    k_values : Iterable[float]
        Slopes for each phase.
    c_values : Iterable[float]
        Critical points for each phase.

    Returns
    -------
    List[float]
        State values after each phase transformation.
    """
    k_vals = list(k_values)
    c_vals = list(c_values)
    if len(k_vals) != 9 or len(c_vals) != 9:
        raise ValueError("Exactly nine parameters required for k_values and c_values")

    p = t
    states = []
    for k, c in zip(k_vals, c_vals):
        p = logistic_function(p, k, c)
        states.append(p)
    return states
