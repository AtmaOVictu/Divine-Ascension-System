"""Ontological agent system with dialogue utilities."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .reason import LogarithmOfReason

__all__ = ["Agent", "philosophical_dialogue", "LogarithmOfReason"]
