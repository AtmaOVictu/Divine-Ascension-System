from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, turns: int = 1) -> List[str]:
    """Simulate a philosophical dialogue and update emotions after each turn."""
    lines: List[str] = []

    for _ in range(turns):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # escalate emotions which may lead to state transitions
        agent1.increase_emotion(0.6)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.increase_emotion(0.6)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    return lines
