"""Public interface for the ``divine_agents`` package."""

from .agent import Agent, OntologyState
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "OntologyState", "philosophical_dialogue"]

