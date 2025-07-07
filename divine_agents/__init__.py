"""Utilities for ontological agent interactions."""

from .agent import Agent
from .dialogue import philosophical_dialogue, philosophical_dialogue_boxed
from .boxes import SymbolicBox

__all__ = ["Agent", "SymbolicBox", "philosophical_dialogue", "philosophical_dialogue_boxed"]
