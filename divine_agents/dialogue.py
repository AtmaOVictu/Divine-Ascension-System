from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 1) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Emotional intensity rises each round, potentially causing state transitions.
    """
    lines: List[str] = []
    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # conversation increases emotional charge
        agent1.update_emotion(0.4)
        agent2.update_emotion(0.4)

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
