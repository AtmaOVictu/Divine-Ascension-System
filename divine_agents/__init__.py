"""Utility package exposing ontological agent classes."""

from .agent import Agent
from .ontology import OntologicalSymbol, OntologicalUnit
from .dialogue import philosophical_dialogue

__all__ = [
    "Agent",
    "OntologicalSymbol",
    "OntologicalUnit",
    "philosophical_dialogue",
]
