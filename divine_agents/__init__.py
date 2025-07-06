"""Divine agent framework for philosophical simulations."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .relative_absolutes import RelativeAbsoluteLibrary
from .metaparadox import MetaparadoxicalModule

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "RelativeAbsoluteLibrary",
    "MetaparadoxicalModule",
]
