"""Utility functions for handling temperature visualization."""

from typing import Tuple


COLOR_BLUE = (0, 0, 1)
COLOR_GREEN = (0, 0.5, 0)
COLOR_YELLOW = (1, 1, 0)
COLOR_RED = (1, 0, 0)
COLOR_GRAY = (0.5, 0.5, 0.5)


def temperature_to_color(temp: float) -> Tuple[float, float, float]:
    """Return an RGB tuple representing the temperature."""
    if temp < 0:
        return COLOR_BLUE
    if 0 <= temp < 25:
        return COLOR_GREEN
    if 25 <= temp < 50:
        return COLOR_YELLOW
    return COLOR_RED


def plot_temperature_change(temps):
    """Plot temperature progression using matplotlib."""
    try:
        import matplotlib.pyplot as plt
    except Exception:  # pragma: no cover - matplotlib optional
        return None
    colors = [temperature_to_color(t) for t in temps]
    plt.scatter(range(len(temps)), [0] * len(temps), color=colors, s=100)
    plt.yticks([])
    plt.xlabel("Čas")
    plt.title("Sprememba Temperature z Barvami")
    return plt
