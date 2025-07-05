from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical dialogue between two agents."""

    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agent1 reacts to agent2's statement
    agent1.update_emotion(0.6)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kako vidiš resnico sedaj?')}")

    # Agent2 responds and possibly evolves further
    agent2.update_emotion(0.8)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Ali je resnica enotna?')}")

    return lines
