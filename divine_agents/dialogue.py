from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8, "anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines


def philosophical_debate(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a dynamic debate reflecting emotional changes."""
    dialogue = philosophical_dialogue(agent1, agent2)

    # Agents react to the last answers with new emotions
    agent1.update_emotion(0.4, "curiosity")
    dialogue.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.7, "fear")
    dialogue.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    dialogue.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    dialogue.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return dialogue
