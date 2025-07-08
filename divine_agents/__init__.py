"""Package exposing main classes and utilities."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .retrieval import build_index, search

__all__ = ["Agent", "philosophical_dialogue", "build_index", "search"]
