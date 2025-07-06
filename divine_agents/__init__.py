"""Convenience access to main classes and helpers."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .language import Language, English, Slovenian, create_language

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "Language",
    "English",
    "Slovenian",
    "create_language",
]
