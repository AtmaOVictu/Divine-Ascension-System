"""Divine Ascension agent framework."""

from .agent import Agent
from .dialogue import philosophical_dialogue

try:  # optional dependency
    from .batch_api import BatchAPI
except Exception:  # pragma: no cover - openai may not be installed in tests
    BatchAPI = None

__all__ = ["Agent", "philosophical_dialogue", "BatchAPI"]
