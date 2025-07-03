"""Dialogue helpers for ontological agents."""

from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def dynamic_debate(
    agent1: Agent,
    agent2: Agent,
    rounds: int = 2,
    increment1: float = 0.4,
    increment2: float = 0.4,
) -> List[str]:
    """Run a debate where emotions influence state transitions.

    Parameters
    ----------
    agent1, agent2:
        Participants in the debate.
    rounds:
        Number of exchanges.
    increment1, increment2:
        How much emotion to add to each agent per round.

    Returns
    -------
    List[str]
        Generated dialogue lines.
    """

    dialogue: List[str] = []
    for _ in range(rounds):
        dialogue.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        dialogue.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(increment1)
        prev_state = agent1.history[-1]
        new_state = agent1.transition()
        if new_state != prev_state:
            dialogue.append(f"{agent1.name} prehaja v stanje: {new_state}")

        agent2.update_emotion(increment2)
        prev_state2 = agent2.history[-1]
        new_state2 = agent2.transition()
        if new_state2 != prev_state2:
            dialogue.append(f"{agent2.name} prehaja v stanje: {new_state2}")

    return dialogue
