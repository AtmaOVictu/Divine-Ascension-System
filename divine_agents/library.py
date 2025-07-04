"""Utility functions for creating and managing word agents."""
from typing import Iterable, List

from .word_agent import WordAgent


def create_word_library(words: Iterable[str]) -> List[WordAgent]:
    """Create a list of WordAgent objects from an iterable of words."""
    return [WordAgent(word) for word in words]
