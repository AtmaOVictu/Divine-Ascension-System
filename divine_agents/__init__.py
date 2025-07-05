"""Agent-based philosophical simulation package."""

from .agent import Agent
from .paradox_agent import ParadoxicalAgent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "ParadoxicalAgent", "philosophical_dialogue"]
