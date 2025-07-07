"""Dialogue helpers and simulation functions."""

from typing import List

from .agent import Agent


def compose_response(agent: Agent, question: str) -> str:
    """Format a line with the agent's current state and answer."""
    return f"{agent.name} ({agent.state}): {agent.respond(question)}"


def apply_emotional_shift(agent: Agent, value: float) -> None:
    """Update an agent's emotion and tension."""
    agent.update_emotion(value)


def handle_state_transition(agent: Agent) -> str:
    """Trigger a state transition and return the new state."""
    return agent.transition()


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    lines.append(compose_response(agent1, "Kaj je resnica?"))
    lines.append(compose_response(agent2, "Kaj je resnica?"))

    apply_emotional_shift(agent1, 0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {handle_state_transition(agent1)}")

    apply_emotional_shift(agent2, 0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {handle_state_transition(agent2)}")

    lines.append(compose_response(agent1, "Kaj je resnica?"))
    lines.append(compose_response(agent2, "Kaj je resnica?"))
    return lines
