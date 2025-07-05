"""Utilities for running dialogues between ontological agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical debate between two agents.

    The agents first answer the question "Kaj je resnica?" from the
    perspective of their current ontological state. Their emotions are then
    increased which may trigger a transition to a new state. The agents
    respond once more after transitioning.
    """

    lines: List[str] = []
    question = "Kaj je resnica?"

    # initial responses
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

    # emotions rise during the exchange
    agent1.update_emotion(0.6)
    agent2.update_emotion(0.8)

    # state transitions
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # responses after transition
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

    return lines
