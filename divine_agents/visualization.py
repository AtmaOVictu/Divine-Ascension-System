from __future__ import annotations

from matplotlib import pyplot as plt

from .agent import Agent


def visualize_agent(agent: Agent):
    """Visualize the agent based on tension and emotion."""
    plt.figure(figsize=(5, 5))
    color_map = {"Ego": "red", "Jaz": "blue", "Enotnost": "green"}
    plt.scatter(agent.tension, agent.emotion, color=color_map.get(agent.state, "black"))
    plt.title(f"Agent: {agent.name}, State: {agent.state}")
    plt.xlabel("Tension")
    plt.ylabel("Emotion")
    return plt
