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


def dynamic_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Generate a dialogue influenced by emotions and transitions."""
    conversation = []
    conversation.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    conversation.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agents react emotionally to the initial exchange
    agent1.update_emotion(0.6)
    agent2.update_emotion(0.4)

    # Perform transitions if thresholds are met
    agent1.transition()
    agent2.transition()

    conversation.append(agent1.reflect_opposites())
    conversation.append(agent2.reflect_opposites())

    return conversation
