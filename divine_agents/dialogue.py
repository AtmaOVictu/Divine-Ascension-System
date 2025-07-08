from typing import List, Tuple
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotion1: Tuple[str, float] = ("anger", 0.6),
    emotion2: Tuple[str, float] = ("joy", 0.6),
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Emotions influence tension and may trigger state transitions.
    """
    lines: List[str] = []

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    agent1.update_emotion(*emotion1)
    prev = agent1.state
    new_state = agent1.transition()
    if new_state != prev:
        lines.append(f"{agent1.name} prehaja v stanje: {new_state}")

    agent2.update_emotion(*emotion2)
    prev = agent2.state
    new_state = agent2.transition()
    if new_state != prev:
        lines.append(f"{agent2.name} prehaja v stanje: {new_state}")

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )
    return lines
