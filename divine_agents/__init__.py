"""Divine agent system package."""

from .agent import Agent
from .dialogue import philosophical_dialogue

try:  # Optional dependency
    from .operating_desk import Codex, operating_desk
except Exception:  # pragma: no cover - Streamlit might not be installed
    Codex = None
    operating_desk = None

__all__ = ["Agent", "philosophical_dialogue", "Codex", "operating_desk"]
