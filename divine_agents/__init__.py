"""Package for ontological agents."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .system import DynamicAgentSystem

__all__ = ["Agent", "philosophical_dialogue", "DynamicAgentSystem"]
