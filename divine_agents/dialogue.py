"""Utilities for simulating philosophical dialogues between agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 3) -> List[str]:
    """Simulate a philosophical dialogue where agents may transition states.

    Each round agents respond according to their current state, experience an
    emotional update and then attempt a state transition based on their new
    emotion and tension levels.

    Parameters
    ----------
    agent1, agent2:
        The participating agents.
    rounds:
        Number of conversational exchanges to simulate.

    Returns
    -------
    List[str]
        Lines of dialogue describing the conversation and transitions.
    """

    lines: List[str] = []
    for _ in range(rounds):
        # Agents respond according to their current ontological states
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Emotions rise as debate continues influencing tension
        agent1.update_emotion(min(1.0, agent1.emotion + 0.4))
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(min(1.0, agent2.emotion + 0.4))
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
