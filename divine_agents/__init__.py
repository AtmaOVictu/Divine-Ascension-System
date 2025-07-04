
"""Top level package for ``divine_agents``.

This exposes the primary :class:`Agent` class and the
``philosophical_dialogue`` function for easy importing.
"""

from .agent import Agent
from .dialogue import philosophical_dialogue

__all__ = ["Agent", "philosophical_dialogue"]

# Optional package version.
__version__ = "0.1.0"
