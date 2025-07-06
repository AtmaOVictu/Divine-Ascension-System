from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements based on current states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotional reactions influence tension and possible transitions
    agent1.update_mood("anger")
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} občuti {agent1.mood} in prehaja v stanje: {agent1.transition()}")

    agent2.update_mood("joy")
    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} občuti {agent2.mood} in prehaja v stanje: {agent2.transition()}")

    # Agents respond again after possible transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
