"""Ontological agents and interactive modules."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .fun import KvizZabavnost, UgankaZabavnost, IgraOdlocanja, Question

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "KvizZabavnost",
    "UgankaZabavnost",
    "IgraOdlocanja",
    "Question",
]
