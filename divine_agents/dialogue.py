from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []

    # Initial exchange based on current states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotional impact of the dialogue
    agent1.update_emotion(0.8)
    new_state_1 = agent1.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {new_state_1}")

    agent2.update_emotion(0.6)
    new_state_2 = agent2.transition()
    lines.append(f"{agent2.name} prehaja v stanje: {new_state_2}")

    # Second exchange after possible transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kako vidiš resnico?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kako vidiš resnico?')}")

    return lines
