"""Convenience imports for divine agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .multi_agents import (
    PhilosophicalResearchAgent,
    EmotionalDynamicAgent,
    MoralDilemmaAgent,
    MultiContextualAgentSystem,
)

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "PhilosophicalResearchAgent",
    "EmotionalDynamicAgent",
    "MoralDilemmaAgent",
    "MultiContextualAgentSystem",
]
