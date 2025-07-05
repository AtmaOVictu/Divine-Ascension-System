"""Convenience exports for the divine agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .orchestrator import AgentDirigent, Zbor, DivinitetniAgent

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "AgentDirigent",
    "Zbor",
    "DivinitetniAgent",
]
