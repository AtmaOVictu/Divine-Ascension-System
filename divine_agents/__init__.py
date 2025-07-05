"""Convenience exports for the divine_agents package.

This module exposes the main :class:`Agent` class along with helper
utilities for philosophical dialogues.  It also provides a simple
"copy" (``agent_precheck``) and "cutter" (``command_filter``) that
can be used to validate or preprocess commands before they are
executed by an agent.
"""

from .agent import Agent
from .dialogue import philosophical_dialogue


def agent_precheck(agent: Agent, command: str) -> str:
    """Check whether a command requires the agent to transition.

    Parameters
    ----------
    agent:
        The agent whose state will be inspected.
    command:
        Command name requesting an action.

    Returns
    -------
    str
        A message describing whether a transition is needed or the
        command can be executed directly.
    """

    if agent.tension > 0.7 or agent.emotion > 0.5:
        return f"Ukaz za {agent.name} potrebuje obravnavo pred prehodom: {command}."
    return f"Ukaz za {agent.name} je sprejet. Izvedba prehoda: {command}"


def command_filter(agent: Agent, command: str) -> str:
    """Filter and process a command based on the agent's state."""

    if command == "prehod" and (agent.tension > 0.7 or agent.emotion > 0.5):
        return agent_precheck(agent, command)
    if command == "respond":
        return agent.respond("Kaj je resnica?")
    return "Ukaz ni prepoznan ali ni v skladu z obstoječimi pravili."


__all__ = [
    "Agent",
    "philosophical_dialogue",
    "agent_precheck",
    "command_filter",
]


