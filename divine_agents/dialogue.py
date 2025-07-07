"""Dialogue utilities for philosophical conversations between agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The function updates each agent's emotional state, checks for possible
    transitions and records their responses.
    """

    lines: List[str] = []
    question = "Kaj je resnica?"

    # Initial responses
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

    # Emotions rise during the debate
    agent1.update_emotion(agent1.emotion + 0.6)
    new_state = agent1.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {new_state}")

    agent2.update_emotion(agent2.emotion + 0.6)
    new_state = agent2.transition()
    lines.append(f"{agent2.name} prehaja v stanje: {new_state}")

    # Final statements reflect new states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

    return lines
