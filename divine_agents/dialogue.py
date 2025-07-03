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

from .moral_agent import MoralAgent


def moral_dialogue(agent1: MoralAgent, agent2: MoralAgent) -> List[str]:
    """Engage two moral agents in a dialogue and reflection."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(agent1.emotion + 0.4)
    agent2.update_emotion(agent2.emotion + 0.4)

    lines.append(agent1.reflect([agent2]))
    lines.append(agent2.reflect([agent1]))

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.decision}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.decision}")
    return lines
