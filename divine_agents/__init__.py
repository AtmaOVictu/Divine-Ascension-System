"""Entry point for the ``divine_agents`` package.

This module exposes the primary :class:`Agent` class and the
``philosophical_dialogue`` function for external use. It simplifies
imports for applications or tests that rely on the agent system.
"""

from .agent import Agent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "philosophical_dialogue"]

