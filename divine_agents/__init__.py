"""Public package interface for the divine_agents module."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .keylock import Key, Lock

__all__ = ["Agent", "Key", "Lock", "philosophical_dialogue"]
