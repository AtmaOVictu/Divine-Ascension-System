"""Package exposing ontological agent utilities."""
from .agent import Agent
from .dialogue import philosophical_dialogue
from .curiosity import CuriousAgent

__all__ = ["Agent", "philosophical_dialogue", "CuriousAgent"]
