import matplotlib.pyplot as plt
from typing import Iterable
from .agent import Agent


def plot_temperature_change(agents: Iterable[Agent]):
    """Display agent temperatures using color-coded scatter plot."""
    temps = [agent.temperature for agent in agents]
    colors = [Agent.temperature_to_color(t) for t in temps]
    plt.scatter(range(len(temps)), [0] * len(temps), color=colors, s=100)
    plt.yticks([])
    plt.xlabel("Agent")
    plt.title("Sprememba Temperature z Barvami")
    plt.show()


def plot_no_color_change():
    """Display placeholder when no color information is available."""
    plt.scatter([0], [0], color="gray", s=100)
    plt.yticks([])
    plt.xlabel("Agent")
    plt.title("Mankanje Barv")
    plt.show()
