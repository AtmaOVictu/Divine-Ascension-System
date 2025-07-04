from typing import List, Tuple
from .agent import Agent
from .insights import SpeedInsights


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> Tuple[List[str], SpeedInsights]:
    """Simulate a short philosophical dialogue between two agents."""
    insights = SpeedInsights()
    lines: List[str] = []

    insights.log_event("start")
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    insights.log_event(f"{agent1.name}_transition")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent1.name} nasprotno stanje: {agent1.activate_opposite_state()}")

    agent2.update_emotion(0.6)
    insights.log_event(f"{agent2.name}_transition")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    lines.append(f"{agent2.name} nasprotno stanje: {agent2.activate_opposite_state()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    insights.log_event("end")
    return lines, insights
