"""Convenience imports for the divine_agents package."""

from .agent import Agent, ReflectiveAgent
from .dialogue import philosophical_dialogue
from .multi_agent_system import MultiAgentSystem

__all__ = [
    "Agent",
    "ReflectiveAgent",
    "philosophical_dialogue",
    "MultiAgentSystem",
]
