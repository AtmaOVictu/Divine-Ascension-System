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

from .recursive_agent import RecursiveAgent


def dynamic_dialogue(agent1: RecursiveAgent, agent2: RecursiveAgent) -> List[str]:
    """Run dialogue with adaptation and reflection influencing transitions."""
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.adapt("conflict")
    agent1.update_emotion(0.8)

    agent2.adapt("ethical_dilemma")
    agent2.update_emotion(0.6)

    agent1.reflect()
    agent2.reflect()

    # second reflection cycle to allow further transitions
    agent1.update_emotion(0.9)
    agent1.reflect()

    lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
