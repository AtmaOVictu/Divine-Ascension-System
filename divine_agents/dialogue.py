from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def decision_process(agents: List[Agent]) -> List[str]:
    """Calculate influence of each agent based on fame and participation."""
    if not agents:
        return []

    total_fame = sum(a.fame for a in agents) or 1
    total_participation = sum(a.participation for a in agents) or 1
    lines = []

    for agent in agents:
        fame_influence = (agent.fame / total_fame) * 100
        participation_influence = (agent.participation / total_participation) * 100
        overall = (fame_influence + participation_influence) / 2
        lines.append(
            f"{agent.name} ima skupni vpliv {overall:.2f}% pri odlocanju."
        )
    return lines
