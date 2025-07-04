"""Ontological agent package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .evolution import evolution_function, transition_res

__all__ = ["Agent", "philosophical_dialogue", "evolution_function", "transition_res"]
