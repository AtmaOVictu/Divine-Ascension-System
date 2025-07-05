"""Convenience access to key components of the divine_agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .utils import logistic_function

__all__ = ["Agent", "philosophical_dialogue", "logistic_function"]
