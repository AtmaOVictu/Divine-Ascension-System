from typing import List, Dict

from .agent import Agent


def decision_process(agents: List[Agent]) -> Dict[str, float]:
    """Compute each agent's influence based on fame and participation."""
    if not agents:
        return {}

    total_fame = sum(agent.fame for agent in agents)
    total_participation = sum(agent.participation for agent in agents)

    influences = {}
    for agent in agents:
        fame_inf = (agent.fame / total_fame) * 100 if total_fame else 0
        part_inf = (agent.participation / total_participation) * 100 if total_participation else 0
        influences[agent.name] = (fame_inf + part_inf) / 2
    return influences
