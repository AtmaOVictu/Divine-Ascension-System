"""Package exposing ontological agents and utilities."""

from .state import OntoState
from .agent import Agent
from .dialogue import philosophical_dialogue

__all__ = ["OntoState", "Agent", "philosophical_dialogue"]
