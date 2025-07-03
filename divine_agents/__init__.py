
"""Core package for the Divine Ascension agent system.

This module exposes the primary classes used throughout the project for
convenience. It allows easy access to :class:`~divine_agents.agent.Agent` and
the :func:`~divine_agents.dialogue.philosophical_dialogue` helper which
facilitate the creation of agents and simulation of their debates.
"""

from .agent import Agent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "philosophical_dialogue"]
