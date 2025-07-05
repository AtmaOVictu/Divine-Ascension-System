"""Ontological agents and helper utilities."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .math_utils import logistic_function, logarithmic_function

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "logistic_function",
    "logarithmic_function",
]

