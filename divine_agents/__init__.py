"""Convenience exports for the divine_agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .dual_agents import CreativeAgent, DestructiveAgent, creative_destructive_interaction

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "CreativeAgent",
    "DestructiveAgent",
    "creative_destructive_interaction",
]
