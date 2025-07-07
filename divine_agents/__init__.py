"""Ontological agent-based system."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .cycle import RecursiveBox

__all__ = ["Agent", "philosophical_dialogue", "RecursiveBox"]
