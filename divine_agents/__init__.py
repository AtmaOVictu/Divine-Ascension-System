"""Top-level package for divine agents.

This module exposes the key classes and helper functions for convenient
import. Users can simply::

    from divine_agents import Agent, philosophical_dialogue
"""

from .agent import Agent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "philosophical_dialogue"]
