from typing import Iterable, List, Tuple
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotions: Iterable[Tuple[str, str]]
) -> List[str]:
    """Simulate a philosophical dialogue influenced by emotional shifts."""
    lines: List[str] = []

    for e1, e2 in emotions:
        agent1.update_emotion(e1)
        agent2.update_emotion(e2)

        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        prev1 = agent1.state
        prev2 = agent2.state
        new1 = agent1.transition()
        new2 = agent2.transition()

        if new1 != prev1:
            lines.append(f"{agent1.name} prehaja v stanje: {new1}")
        if new2 != prev2:
            lines.append(f"{agent2.name} prehaja v stanje: {new2}")

    return lines
