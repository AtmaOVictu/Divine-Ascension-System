"""Ontological agent framework."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .cycle import OuroborosCycle

__all__ = ["Agent", "philosophical_dialogue", "OuroborosCycle"]
