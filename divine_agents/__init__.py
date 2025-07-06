"""Ontological agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue, transition_to_symbol

__all__ = ["Agent", "philosophical_dialogue", "transition_to_symbol"]
