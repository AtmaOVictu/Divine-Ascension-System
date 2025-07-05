from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue where agents may transition states."""
    lines: List[str] = []

    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.adjust_emotion(0.3)
        agent2.adjust_emotion(0.3)

        prev1, prev2 = agent1.state, agent2.state
        new1, new2 = agent1.transition(), agent2.transition()

        if new1 != prev1:
            lines.append(f"{agent1.name} prehaja v stanje: {new1}")
        if new2 != prev2:
            lines.append(f"{agent2.name} prehaja v stanje: {new2}")

    return lines
