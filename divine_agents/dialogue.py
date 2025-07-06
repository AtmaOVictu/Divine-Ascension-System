"""Dialogue utilities for philosophical agent interactions."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2:
        Interacting agents.
    rounds:
        Number of conversational rounds.
    """

    lines: List[str] = []
    for r in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Emotions evolve during discussion
        agent1.perceive_emotion('anger', 0.6 + 0.2 * r)
        new_state = agent1.transition()
        lines.append(f"{agent1.name} prehaja v stanje: {new_state}")

        agent2.perceive_emotion('joy', 0.3 + 0.1 * r)
        new_state = agent2.transition()
        lines.append(f"{agent2.name} prehaja v stanje: {new_state}")

    # Final reflections after conversation
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
