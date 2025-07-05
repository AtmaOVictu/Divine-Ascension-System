"""Ontological agent package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .generator import Generator

__all__ = ["Agent", "Generator", "philosophical_dialogue"]
