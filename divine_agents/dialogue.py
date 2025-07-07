"""Utilities for generating short philosophical dialogues between agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The function updates each agent's emotional state which may trigger
    a transition of their ontological state. The resulting dialogue reflects
    both their philosophical position and their emotions.
    """

    lines: List[str] = []

    # Initial statements
    lines.append(
        f"{agent1.name} ({agent1.state}, {agent1.emotion_type}): "
        f"{agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}, {agent2.emotion_type}): "
        f"{agent2.respond('Kaj je resnica?')}"
    )

    # Emotions rise as debate continues
    agent1.update_emotion(0.8, "jeza")
    new_state1 = agent1.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {new_state1}")

    agent2.update_emotion(0.6, "sočutje")
    new_state2 = agent2.transition()
    lines.append(f"{agent2.name} prehaja v stanje: {new_state2}")

    # Second round of answers after the transition
    lines.append(
        f"{agent1.name} ({agent1.state}, {agent1.emotion_type}): "
        f"{agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}, {agent2.emotion_type}): "
        f"{agent2.respond('Kaj je resnica?')}"
    )

    return lines
