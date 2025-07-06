from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical dialogue and trigger state transitions."""
    lines: List[str] = []
    for _ in range(10):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(0.1)
        agent2.update_emotion(0.1)

        previous = agent1.state
        agent1.transition()
        if agent1.state != previous:
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

        previous = agent2.state
        agent2.transition()
        if agent2.state != previous:
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

        if agent1.state == "Enotnost" or agent2.state == "Enotnost":
            break
    return lines
