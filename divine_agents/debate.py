from typing import List

from .agent import Agent


def ontological_debate(agent1: Agent, agent2: Agent) -> List[str]:
    """Conduct an ontological debate between two agents.

    Agents exchange philosophical views and escalate their emotions,
    potentially triggering state transitions.
    """
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    for _ in range(2):
        # escalate emotional intensity
        agent1.update_emotion(agent1.emotion + 0.4)
        agent2.update_emotion(agent2.emotion + 0.4)

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
