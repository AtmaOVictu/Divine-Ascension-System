"""Ontology based agent system."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .simulation import dynamic_philosophical_debate

__all__ = ["Agent", "philosophical_dialogue", "dynamic_philosophical_debate"]
