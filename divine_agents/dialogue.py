from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotion rises during discussion
    agent1.update_emotion(0.8, label="anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, label="joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Responses after emotional shift
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines


def philosophical_debate(agent1: Agent, agent2: Agent) -> List[str]:
    """Extended debate showing multiple transitions based on tension."""
    conversation: List[str] = []

    # Opening
    conversation.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    conversation.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Increase tension and emotions, potentially causing transitions
    agent1.update_emotion(0.6, label="fear")
    agent2.update_emotion(0.5, label="joy")
    conversation.append(f"{agent1.name} -> {agent1.transition()}")
    conversation.append(f"{agent2.name} -> {agent2.transition()}")

    # Second round
    conversation.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    conversation.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Final emotional surge
    agent1.update_emotion(0.8, label="joy")
    agent2.update_emotion(0.9, label="anger")
    conversation.append(f"{agent1.name} -> {agent1.transition()}")
    conversation.append(f"{agent2.name} -> {agent2.transition()}")

    conversation.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    conversation.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return conversation
