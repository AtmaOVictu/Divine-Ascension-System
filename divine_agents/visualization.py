"""Simple matplotlib based agent visualization."""

from __future__ import annotations

from typing import Optional

import matplotlib.pyplot as plt

from .agent import Agent


def visualize_agent(agent: Agent) -> None:
    """Visualize an agent on a tension/emotion plane."""
    color_map = {"Ego": "red", "Jaz": "blue", "Enotnost": "green"}
    plt.figure(figsize=(5, 5))
    plt.scatter(agent.tension, agent.emotion, color=color_map.get(agent.state, "black"))
    plt.title(f"Agent: {agent.name}, State: {agent.state}")
    plt.xlabel("Tension")
    plt.ylabel("Emotion")
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.close()
