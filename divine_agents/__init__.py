"""High-level package for ontological agents."""

from .agent import Agent
from .dialogue import philosophical_dialogue, dynamic_debate
from .special_agents import (
    AgentNEZNANKA,
    AgentNEZNANKA_ZVOK,
    AgentPI,
    AgentROM,
)

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "dynamic_debate",
    "AgentNEZNANKA",
    "AgentNEZNANKA_ZVOK",
    "AgentPI",
    "AgentROM",
]

