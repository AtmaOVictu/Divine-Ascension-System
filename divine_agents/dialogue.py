from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Each agent responds based on its current ontological state and emotion. The
    dialogue then intensifies emotions, causing possible state transitions, and
    the agents reply again from their new perspective.
    """
    lines: List[str] = []

    # Initial exchange
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotional shift leading to potential transitions
    agent1.update_emotion(0.8, "anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "fear")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second exchange after emotions affected their states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
