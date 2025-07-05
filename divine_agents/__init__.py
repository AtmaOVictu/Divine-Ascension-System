"""Divine Agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .discourse import TruthDiscourse
from .phononto import FonontoTransition
from .emotions import EMOTIONS

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "TruthDiscourse",
    "FonontoTransition",
    "EMOTIONS",
]
