from typing import List

from .agent import Agent


def emotional_conversation(agent1: Agent, agent2: Agent) -> List[str]:
    """Conduct a short conversation influenced by agents' emotions."""
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.emotive_respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.emotive_respond('Kaj je resnica?')}")

    agent1.set_emotion('anger', 0.6)
    agent2.set_emotion('joy', 0.4)

    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.emotive_respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.emotive_respond('Kaj je resnica?')}")

    return lines
