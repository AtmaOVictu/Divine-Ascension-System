"""Ontological agent system package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .generator import Generator

__all__ = ["Agent", "philosophical_dialogue", "Generator"]
