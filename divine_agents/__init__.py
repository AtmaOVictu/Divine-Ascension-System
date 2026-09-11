"""Package exposing core agent classes and utilities."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .boxes import EgoBox, JazBox, EnotnostBox

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "EgoBox",
    "JazBox",
    "EnotnostBox",
]

