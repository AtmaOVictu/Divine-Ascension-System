"""Utility functions to simulate philosophical dialogues between agents."""
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> list[str]:
    """Simulate a short dialogue and return the conversation lines."""
    conversation = []
    conversation.append(f"{agent1.name} ({agent1.state}): {agent1.philosophical_response()}")
    conversation.append(f"{agent2.name} ({agent2.state}): {agent2.philosophical_response()}")

    # Agents respond and may transition based on heightened emotions
    agent1.update_emotion(agent1.emotion + 0.4)
    agent2.update_emotion(agent2.emotion + 0.3)

    conversation.append(f"{agent1.name} ({agent1.state}): {agent1.philosophical_response()}")
    conversation.append(f"{agent2.name} ({agent2.state}): {agent2.philosophical_response()}")

    return conversation
