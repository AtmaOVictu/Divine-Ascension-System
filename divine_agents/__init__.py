"""Divine Agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .multi_interaction import multi_agent_debate

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "multi_agent_debate",
]
