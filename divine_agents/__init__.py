"""Top level package for the Divine Ascension system.

Available components
--------------------
- ``Agent`` -- ontological agent capable of state transitions driven by
  emotion and tension.
- ``philosophical_dialogue`` -- helper function that orchestrates a short
  debate between two agents.
"""

from .agent import Agent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "philosophical_dialogue"]
