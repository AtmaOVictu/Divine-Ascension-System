"""Utility to simulate philosophical dialogues between agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Run a small dialogue and trigger emotional state changes."""

    lines: List[str] = []
    question = "Kaj je resnica?"

    # Initial responses
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

    # Emotional reactions to each other's answers
    agent1.update_emotion(agent1.emotion + 0.6)
    agent2.update_emotion(agent2.emotion + 0.6)

    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final responses after potential transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

    return lines
