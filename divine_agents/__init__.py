"""Convenience exports for the divine_agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue


def agent_precheck(agent: Agent, command: str) -> str:
    """Check whether a command requires additional handling based on the agent's state."""
    if agent.tension > 0.7 or agent.emotion > 0.5:
        return f"Ukaz za {agent.name} potrebuje obravnavo pred prehodom: {command}."
    return f"Ukaz za {agent.name} je sprejet. Izvedba prehoda: {command}"


def command_filter(agent: Agent, command: str) -> str:
    """Filter commands and perform pre-checks or responses."""
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

