"""Dialogue utilities for ontological agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""

    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('What is truth?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('What is truth?')}")

    # Emotions rise during the debate
    agent1.update_emotion(0.8, "anger")
    agent2.update_emotion(0.6, "curiosity")
    lines.append(f"{agent1.name} transitions to: {agent1.transition()}")
    lines.append(f"{agent2.name} transitions to: {agent2.transition()}")

    # Agents respond again from their new states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('And now?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('And now?')}")

    return lines
