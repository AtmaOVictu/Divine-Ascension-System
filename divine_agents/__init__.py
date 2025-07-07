"""Package for ontological agents."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .sub_agent import SubAgent

__all__ = ["Agent", "SubAgent", "philosophical_dialogue"]
