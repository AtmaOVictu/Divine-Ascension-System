from typing import List
from .agent import Agent


def ontological_debate(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a debate where agents may change state based on emotion."""
    lines = []
    for i in range(rounds):
        # Agents state their current view on truth
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # escalate emotions to trigger potential transitions
        agent1.update_emotion(0.4 + 0.2 * i)
        agent2.update_emotion(0.3 + 0.3 * i)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    return lines
