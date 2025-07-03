"""Utility functions for calculating differences and interpolating values."""

from typing import List


# Type alias for readability
Number = float


def compute_differences(agent1, agent2) -> dict:
    """Return emotion and tension differences between two agents."""
    return {
        "emotion_diff": agent1.emotion - agent2.emotion,
        "tension_diff": agent1.tension - agent2.tension,
    }


def linear_interpolation(x: List[Number], y: List[Number], new_x: List[Number]) -> List[Number]:
    """Perform simple piecewise linear interpolation."""
    if len(x) != len(y):
        raise ValueError("x and y must be of equal length")
    if sorted(x) != x:
        raise ValueError("x values must be sorted")

    result = []
    for xi in new_x:
        if xi <= x[0]:
            result.append(y[0])
        elif xi >= x[-1]:
            result.append(y[-1])
        else:
            for idx in range(1, len(x)):
                if xi <= x[idx]:
                    x0, x1 = x[idx - 1], x[idx]
                    y0, y1 = y[idx - 1], y[idx]
                    t = (xi - x0) / (x1 - x0)
                    result.append(y0 + t * (y1 - y0))
                    break
    return result


def quadratic_interpolation(x: List[Number], y: List[Number], new_x: List[Number]) -> List[Number]:
    """Quadratic interpolation using the Lagrange polynomial."""
    if len(x) != 3 or len(y) != 3:
        raise ValueError("Quadratic interpolation requires exactly three data points")
    if sorted(x) != x:
        raise ValueError("x values must be sorted")
    x0, x1, x2 = x
    y0, y1, y2 = y
    result = []
    for xi in new_x:
        term0 = y0 * (xi - x1) * (xi - x2) / ((x0 - x1) * (x0 - x2))
        term1 = y1 * (xi - x0) * (xi - x2) / ((x1 - x0) * (x1 - x2))
        term2 = y2 * (xi - x0) * (xi - x1) / ((x2 - x0) * (x2 - x1))
        result.append(term0 + term1 + term2)
    return result
