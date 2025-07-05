"""Ontology-based agent package."""

from .agent import Agent
from .entities import ShadowAgent, AngelAgent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "ShadowAgent", "AngelAgent", "philosophical_dialogue"]
