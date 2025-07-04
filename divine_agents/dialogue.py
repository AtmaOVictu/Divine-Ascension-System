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

from .multicolor_agent import MultiColorAgent


def colorful_philosophical_dialogue(agent1: MultiColorAgent, agent2: MultiColorAgent) -> List[str]:
    """Simulate dialogue between two MultiColorAgents including colors."""
    lines = []
    lines.append(
        f"{agent1.name} ({agent1.state}, {agent1.color}, {agent1.visibility}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}, {agent2.color}, {agent2.visibility}): {agent2.respond('Kaj je resnica?')}"
    )

    agent1.update_emotion(0.8)
    lines.append(
        f"{agent1.name} prehaja v stanje: {agent1.transition()} ({agent1.color}, {agent1.visibility})"
    )

    agent2.update_emotion(0.6)
    lines.append(
        f"{agent2.name} prehaja v stanje: {agent2.transition()} ({agent2.color}, {agent2.visibility})"
    )

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
