"""Utilities for running philosophical dialogues between agents."""

from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The conversation adjusts each agent's emotion, potentially causing
    state transitions. Returned lines describe the full interaction.
    """

    lines: List[str] = []

    # Initial statements about truth
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions rise during the debate
    agent1.update_emotion(0.8, "anger")
    lines.append(f"{agent1.name} čuti {agent1.emotion_type}.")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "joy")
    lines.append(f"{agent2.name} čuti {agent2.emotion_type}.")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final reflections on truth in the new states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
