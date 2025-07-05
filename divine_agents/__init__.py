"""Package exposing core agent functionality."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .logistic import logistic_transition

__all__ = ["Agent", "philosophical_dialogue", "logistic_transition"]
