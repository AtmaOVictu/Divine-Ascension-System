"""Public API for divine_agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .codex_self import CodexSelf, EmotionalDialogue

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "CodexSelf",
    "EmotionalDialogue",
]
