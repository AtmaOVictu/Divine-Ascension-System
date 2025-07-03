"""Dialogue utilities for ontological agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, turns: int = 2, intensity: float = 0.6) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2:
        The agents engaging in the conversation.
    turns:
        Number of conversational turns to perform.
    intensity:
        Emotion intensity applied during each interaction.
    """

    lines: List[str] = []
    speaker, listener = agent1, agent2
    for _ in range(turns):
        lines.append(f"{speaker.name} ({speaker.state}): {speaker.respond('Kaj je resnica?')}")
        listener.interact(speaker, intensity)
        lines.append(f"{listener.name} prehaja v stanje: {listener.state}")
        speaker, listener = listener, speaker

    return lines
