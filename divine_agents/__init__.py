"""Top-level package for divine agents system."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .debate import run_debate

__all__ = ["Agent", "philosophical_dialogue", "run_debate"]
