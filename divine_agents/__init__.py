"""Utility package for the Divine Ascension system."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .ontoprocesor import MetaEgo, MetaJaz, Bog, OntoProcesor

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "MetaEgo",
    "MetaJaz",
    "Bog",
    "OntoProcesor",
]
