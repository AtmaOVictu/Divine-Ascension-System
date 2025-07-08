from typing import List
from .agent import Agent
from .reputation import ReputationSystem


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

    rep = ReputationSystem()
    rep.interact(agent1, agent2, action="help")
    lines.append(f"{agent1.name} fama: {agent1.fame} ({agent1.fame_tier()})")
    lines.append(f"{agent2.name} fama: {agent2.fame} ({agent2.fame_tier()})")
    return lines
