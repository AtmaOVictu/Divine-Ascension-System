"""Utilities for simulating philosophical dialogues between agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""

    lines: List[str] = []

    # initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('truth?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('truth?')}")

    # update emotions based on discussion
    agent1.update_emotion("anger", 0.8)
    lines.append(f"{agent1.name} evolves to: {agent1.transition()}")

    agent2.update_emotion("joy", 0.6)
    lines.append(f"{agent2.name} evolves to: {agent2.transition()}")

    # final responses after potential transitions
    lines.append(f"{agent1.name}: {agent1.respond('truth?')}")
    lines.append(f"{agent2.name}: {agent2.respond('truth?')}")

    return lines
