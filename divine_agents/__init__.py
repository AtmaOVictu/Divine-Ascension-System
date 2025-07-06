"""Expose package classes for easy access."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .phonetics import PhoneticTruthMap

__all__ = ["Agent", "philosophical_dialogue", "PhoneticTruthMap"]
