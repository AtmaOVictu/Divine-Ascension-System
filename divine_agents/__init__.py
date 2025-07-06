"""Ontological debate system package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .debate import OntologicalDebate

__all__ = ["Agent", "philosophical_dialogue", "OntologicalDebate"]
