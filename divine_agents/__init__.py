"""Core package for divine agent simulations."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .ecosystem import Ecosystem, EcosystemRecord

__all__ = ["Agent", "philosophical_dialogue", "Ecosystem", "EcosystemRecord"]
