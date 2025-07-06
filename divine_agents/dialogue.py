"""Utilities for simulating philosophical debates between agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate an emotional philosophical dialogue between two agents."""

    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agents exchange ideas influencing their emotions and tension
    agent1.update_emotion(0.4)
    agent2.update_emotion(0.6)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # Agent 1 considers wisdom key after hearing Agent 2
    agent1.set_key("wisdom")
    lines.append(f"{agent1.name} (po kljucu): {agent1.state}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
