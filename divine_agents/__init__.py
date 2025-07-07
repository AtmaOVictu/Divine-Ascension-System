"""Divine Agents package for simulating philosophical dialogues.

This package provides an ontological framework where agents transition
between states (Ego, Jaz, Enotnost) based on emotions and tension.
It exposes the :class:`~divine_agents.agent.Agent` class for modeling
such entities and the :func:`~divine_agents.dialogue.philosophical_dialogue`
function to orchestrate their conversations.
"""

from .agent import Agent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "philosophical_dialogue"]

__version__ = "0.1.0"
