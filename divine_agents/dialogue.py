from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue where emotions drive transitions."""

    lines: List[str] = []

    for i in range(rounds):
        # Each agent states their view on truth according to their current state
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Emotional escalation influences future transitions
        if i == 0:
            agent1.feel('anger', 0.6)
            agent2.feel('joy', 0.4)
        else:
            agent1.feel('fear', 0.2)
            agent2.feel('joy', 0.4)

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
