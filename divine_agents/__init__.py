"""Divine Agents package.

This package implements an ontological agent system capable of transitioning
between philosophical states (Ego, Jaz, Enotnost) in response to emotional
intensity and tension. It exposes the :class:`Agent` class and the
``philosophical_dialogue`` helper used to orchestrate dialogues among agents.
"""

from .agent import Agent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "philosophical_dialogue"]
