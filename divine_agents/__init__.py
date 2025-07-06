"""Ontological agent package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .conversation import multi_turn_dialogue

__all__ = ["Agent", "philosophical_dialogue", "multi_turn_dialogue"]
