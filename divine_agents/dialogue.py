from typing import List
from .agent import Agent
from .decision import DecisionMaker


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    dm1 = DecisionMaker(agent1)
    lines.append(f"{agent1.name} prehaja v stanje: {dm1.decide_transition()}")

    agent2.update_emotion(0.6)
    dm2 = DecisionMaker(agent2)
    lines.append(f"{agent2.name} prehaja v stanje: {dm2.decide_transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
