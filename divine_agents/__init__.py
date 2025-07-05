"""Package exposing divine agent components."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .fononto import FonontoTransition, OntologicalPhase

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "FonontoTransition",
    "OntologicalPhase",
]
