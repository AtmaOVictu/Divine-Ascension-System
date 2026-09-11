"""Tools for generating short philosophical conversations."""

from typing import Iterable, List
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    actions1: Iterable[str] = ("bad", "bad"),
    actions2: Iterable[str] = ("bad", "bad"),
) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1, agent2:
        Participants in the dialogue.
    actions1, actions2:
        Sequences of actions each agent performs in turn. Actions influence
        emotion and tension which may trigger state transitions.
    """

    lines = [
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}",
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}",
    ]

    for act1, act2 in zip(actions1, actions2):
        agent1.perform_action(act1)
        agent2.perform_action(act2)
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
