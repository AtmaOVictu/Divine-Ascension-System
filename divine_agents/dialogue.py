from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # escalate emotions which may trigger state transitions
        agent1.update_emotion('anger', 0.8)
        agent2.update_emotion('joy', 0.6)

        if agent1.transition() != agent1.history[-2]:
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

        if agent2.transition() != agent2.history[-2]:
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    return lines
