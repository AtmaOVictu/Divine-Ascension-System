from typing import List
from .dynamic_agent import DynamicAgent


def dynamic_debate(agent1: DynamicAgent, agent2: DynamicAgent) -> List[str]:
    """Simulate a debate where agents may change state via emotions and keys."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agents influence each other, raising emotion
    agent1.update_emotion(0.6)
    agent2.update_emotion(0.6)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # key based activation
    agent1.set_key('wisdom')
    lines.append(f"{agent1.name} aktiviran s kljucem 'wisdom': {agent1.state}")
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
