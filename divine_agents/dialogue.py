from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue where emotions drive transitions."""
    lines: List[str] = []

    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # escalate emotions influencing tension
        agent1.update_emotion(min(agent1.emotion + 0.3, 1.0), "jeza")
        agent2.update_emotion(min(agent2.emotion + 0.2, 1.0), "presenečenje")

        before1, before2 = agent1.state, agent2.state
        new1 = agent1.transition()
        new2 = agent2.transition()

        if new1 != before1:
            lines.append(f"{agent1.name} prehaja v stanje: {new1}")
        if new2 != before2:
            lines.append(f"{agent2.name} prehaja v stanje: {new2}")

    return lines
