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

from .multilingual_agent import MultilingualAgent


def multilingual_dialogue(agent1: MultilingualAgent, agent2: MultilingualAgent) -> List[str]:
    """Dialogue between multilingual agents reflecting emotional evolution."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('What is truth?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('What is truth?')}")

    agent1.evolve()
    lines.append(f"{agent1.name} transitions to: {agent1.state}")

    agent2.evolve()
    lines.append(f"{agent2.name} transitions to: {agent2.state}")

    lines.append(f"{agent1.name}: {agent1.respond('What is truth?')}")
    lines.append(f"{agent2.name}: {agent2.respond('What is truth?')}")
    return lines
