from typing import List
from .agent import Agent


def dynamic_conversation(agent1: Agent, agent2: Agent, rounds: int = 3) -> List[str]:
    """Simulate a dialogue where agents adjust emotion and may change states."""
    lines: List[str] = []
    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # escalate emotions differently for each agent
        agent1.apply_emotion(agent1.emotion + 0.3, 'anger')
        agent2.apply_emotion(agent2.emotion + 0.2, 'joy')

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
