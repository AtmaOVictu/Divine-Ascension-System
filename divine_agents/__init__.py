"""Public API for the divine_agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue, group_dialogue
from .groups import AgentGroup

__all__ = [
    "Agent",
    "AgentGroup",
    "philosophical_dialogue",
    "group_dialogue",
]

