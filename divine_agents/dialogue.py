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

from .self_deception_agent import SelfDeceptionAgent


def deception_dialogue(agent: SelfDeceptionAgent, other: Agent) -> List[str]:
    """Dialogue demonstrating self-deception resisting change."""
    lines = []
    lines.append(f"{agent.name} ({agent.state}): {agent.respond('Kaj je resnica?')}")
    lines.append(f"{other.name} ({other.state}): {other.respond('Kaj je resnica?')}")

    agent.update_emotion(0.8)
    lines.append(f"{agent.name} poskusa ostati v stanju: {agent.transition()}")

    other.update_emotion(0.6)
    lines.append(f"{other.name} prehaja v stanje: {other.transition()}")

    lines.append(f"{agent.name}: {agent.respond('Kaj je resnica?')}")
    lines.append(f"{other.name}: {other.respond('Kaj je resnica?')}")
    return lines
