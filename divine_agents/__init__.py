"""Divine agents package providing agent classes and utilities."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .manager import ManagerAgent, SubAgent

__all__ = ["Agent", "philosophical_dialogue", "ManagerAgent", "SubAgent"]
