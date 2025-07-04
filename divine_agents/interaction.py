"""Utilities for running philosophical dialogues between agents."""

from typing import List

from .agent import Agent


def run_dialogue(agent1: Agent, agent2: Agent, question: str) -> List[str]:
    """Run a dialogue step where each agent responds and may transition."""
    conversation = []
    conversation.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond(question)}"
    )
    conversation.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond(question)}"
    )

    # Increase emotional tension to simulate debate intensity
    agent1.update_emotion(agent1.emotion + 0.8)
    agent2.update_emotion(agent2.emotion + 0.8)

    new_state1 = agent1.transition()
    new_state2 = agent2.transition()

    conversation.append(f"{agent1.name} prehaja v stanje: {new_state1}")
    conversation.append(f"{agent2.name} prehaja v stanje: {new_state2}")

    conversation.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond(question)}"
    )
    conversation.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond(question)}"
    )

    return conversation
