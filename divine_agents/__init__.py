"""Public package interface for divine agents."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .operations import RESOperations

__all__ = ["Agent", "philosophical_dialogue", "RESOperations"]
