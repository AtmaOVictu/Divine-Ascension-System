"""Initialization for the divine agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .ego import Ego
from .ontoznano import Ontoznano
from .knowledge_base import KnowledgeBase
from .modul import Modul
from .codex import Codex

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "Ego",
    "Ontoznano",
    "KnowledgeBase",
    "Modul",
    "Codex",
]

