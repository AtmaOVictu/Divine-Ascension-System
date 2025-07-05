"""Convenience exports for the divine_agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue


def agent_precheck(agent: Agent, command: str) -> str:
    """Check whether a transition is required before executing ``command``."""
    if agent.tension > 0.7 or agent.emotion > 0.5:
        new_state = agent.transition()
        return (
            f"{agent.name} prehaja v stanje {new_state} pred ukazom {command}."
        )
    return f"{agent.name} ostaja v stanju {agent.state} za ukaz {command}."


def command_filter(agent: Agent, command: str) -> str:
    """Filter and execute commands according to agent state and urgency."""
    if command == "prehod":
        return agent_precheck(agent, command)
    if command == "respond":
        return agent.respond("Kaj je resnica?")
    return "Ukaz ni prepoznan."

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "agent_precheck",
    "command_filter",
]

