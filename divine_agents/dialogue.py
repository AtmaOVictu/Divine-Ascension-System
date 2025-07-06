"""Utilities for simulating philosophical dialogue between agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""

    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('What is truth?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('What is truth?')}")

    # Agents react emotionally to the initial statements
    agent1.update_emotion(0.8)
    lines.append(
        f"{agent1.name} feels {agent1._emotion_label()} and transitions to: {agent1.transition()}"
    )

    agent2.update_emotion(0.6)
    lines.append(
        f"{agent2.name} feels {agent2._emotion_label()} and transitions to: {agent2.transition()}"
    )

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('What is truth?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('What is truth?')}")
    return lines
