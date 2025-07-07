"""Package exposing agents and dialogue helpers."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .insertion import InsertionAgent

__all__ = ["Agent", "InsertionAgent", "philosophical_dialogue"]
