"""Public API for the divine_agents package."""

from .agent import Agent
from .manager import ManagerAgent, SubAgent
from .dialogue import philosophical_dialogue, managed_dialogue

__all__ = [
    "Agent",
    "ManagerAgent",
    "SubAgent",
    "philosophical_dialogue",
    "managed_dialogue",
]
