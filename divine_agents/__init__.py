"""Ontological agents and task management utilities."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .krak import Krak, KrakManager

__all__ = ["Agent", "philosophical_dialogue", "Krak", "KrakManager"]
