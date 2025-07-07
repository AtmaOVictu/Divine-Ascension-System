from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, steps: int = 2) -> List[str]:
    """Simulate a philosophical dialogue where agents may transition states."""
    lines: List[str] = []
    for step in range(steps):
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        if step == 0:
            agent1.update_emotion(0.8, "strah")
            agent2.update_emotion(0.6, "veselje")
        else:
            agent1.update_emotion(0.4)
            agent2.update_emotion(0.2)

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    return lines
