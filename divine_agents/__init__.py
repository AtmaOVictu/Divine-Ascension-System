"""Agent framework for philosophical state transitions."""

from .agent import Agent
from .resonance_agent import ResonanceAgent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "ResonanceAgent", "philosophical_dialogue"]
