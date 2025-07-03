from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue where emotions drive state changes."""
    lines: List[str] = []

    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(agent1.emotion + 0.4)
        previous = agent1.state
        agent1.transition()
        if agent1.state != previous:
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

        agent2.update_emotion(agent2.emotion + 0.4)
        previous = agent2.state
        agent2.transition()
        if agent2.state != previous:
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    return lines
