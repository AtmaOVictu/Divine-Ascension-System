"""Init file for divine agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .connotation import Category, categorize_words

__all__ = ["Agent", "philosophical_dialogue", "Category", "categorize_words"]
