from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    agent1.update_fame(1, 0, agent1.participation)
    agent2.update_fame(1, 0, agent2.participation)

    return lines


def decision_process(agents: List[Agent]) -> List[float]:
    """Return influence percentages for agents based on fame and participation."""
    total_fame = sum(a.fame for a in agents) or 1
    total_participation = sum(a.participation for a in agents) or 1

    influences = []
    for agent in agents:
        fame_inf = (agent.fame / total_fame) * 100
        part_inf = (agent.participation / total_participation) * 100
        influences.append((fame_inf + part_inf) / 2)
    return influences
