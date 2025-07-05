from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, steps: int = 2) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    for step in range(1, steps + 1):
        agent1.update_emotion(min(agent1.emotion + 0.4, 1.0))
        agent1.logistic_update(step / steps, k=2.0, c=0.5)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(min(agent2.emotion + 0.3, 1.0))
        agent2.logistic_update(step / steps, k=2.0, c=0.5)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
