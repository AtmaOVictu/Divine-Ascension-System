"""Package exposing agent classes and utilities."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .logger import SimpleErrorLogger

__all__ = ["Agent", "philosophical_dialogue", "SimpleErrorLogger"]
