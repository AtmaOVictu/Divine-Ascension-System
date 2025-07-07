from typing import List

from .agent import Agent
from .membership import MembershipAgent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def dynamic_dialogue(agent1: MembershipAgent, agent2: MembershipAgent) -> List[str]:
    """Extended dialogue illustrating membership transitions and emotions."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.9)
    agent2.update_emotion(0.6)
    lines.append(f"{agent1.name} tension: {agent1.tension:.1f}")
    lines.append(f"{agent2.name} tension: {agent2.tension:.1f}")

    agent1.transition(agent2)
    agent2.transition(agent1)
    lines.append(f"{agent1.name} state: {agent1.state}")
    lines.append(f"{agent2.name} state: {agent2.state}")

    return lines
