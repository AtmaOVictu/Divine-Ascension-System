from typing import List
from .moral_agent import MoralAgent


def moral_dialogue(agent1: MoralAgent, agent2: MoralAgent) -> List[str]:
    """Simulate dialogue including moral decisions between two moral agents."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    decision1 = agent1.make_decision([agent2])
    decision2 = agent2.make_decision([agent1])
    lines.append(f"{agent1.name} se odloča: {decision1}")
    lines.append(f"{agent2.name} se odloča: {decision2}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
