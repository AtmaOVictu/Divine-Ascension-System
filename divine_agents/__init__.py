"""Divine agents package."""

from .agent import Agent
from .wide_narrow import WideAgent, NarrowAgent, debate

__all__ = ["Agent", "WideAgent", "NarrowAgent", "debate"]
