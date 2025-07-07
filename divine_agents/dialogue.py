from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial responses based on current states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.speak('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.speak('Kaj je resnica?')}")

    # Emotional impact from the discussion triggers possible transitions
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.experience(0.8)}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.experience(0.6)}")

    # Responses after potential state changes
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.speak('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.speak('Kaj je resnica?')}")

    return lines
