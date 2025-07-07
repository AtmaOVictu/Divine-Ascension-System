"""Utilities for simulating dialogues between ontological agents."""

from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Each round both agents respond to the question "What is truth?". After
    responding their emotion and tension are updated which may trigger a
    transition in ontological state.
    """

    lines: List[str] = []
    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('What is truth?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('What is truth?')}")

        agent1.update_emotion(min(agent1.emotion + 0.4, 1.0), 'anger')
        lines.append(f"{agent1.name} transitions to: {agent1.transition()}")

        agent2.update_emotion(min(agent2.emotion + 0.3, 1.0), 'joy')
        lines.append(f"{agent2.name} transitions to: {agent2.transition()}")

    return lines
