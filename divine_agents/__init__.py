"""Public interface for divine_agents package."""

from .agent import Agent
from .krak import Krak
from .system import CodexSystem
from .dialogue import philosophical_dialogue, emotional_dialogue

__all__ = [
    "Agent",
    "Krak",
    "CodexSystem",
    "philosophical_dialogue",
    "emotional_dialogue",
]
