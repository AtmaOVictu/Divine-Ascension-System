from typing import List
from .agent import Agent
from .opposite import OppositeAgent


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


def opposite_debate(agent: Agent, opposite: OppositeAgent) -> List[str]:
    """Engage an agent in debate with its opposite concept."""
    agent.define_opposite(opposite)
    lines = [f"{agent.name} ({agent.state}) za\u010dna debato z nasprotjem {opposite.name}."]
    lines.extend(agent.debate())
    return lines
