"""Convenience imports for the divine agent system."""

from .agent import Agent

try:
    from .dialogue_manager import DialogueManager
except Exception:  # pragma: no cover - during partial installs
    DialogueManager = None

__all__ = ["Agent", "DialogueManager"]
