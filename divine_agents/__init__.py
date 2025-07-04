"""Public API for the divine agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .cli import run_dialogue

__all__ = ["Agent", "philosophical_dialogue", "run_dialogue"]
