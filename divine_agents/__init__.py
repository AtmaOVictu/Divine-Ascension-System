"""High-level API for the divine agents package."""

from .agent import Agent, AgentWithHistory
from .dialogue import philosophical_dialogue, run_simulation
from .emotional_contagion import EmotionalContagion

__all__ = [
    "Agent",
    "AgentWithHistory",
    "EmotionalContagion",
    "philosophical_dialogue",
    "run_simulation",
]

