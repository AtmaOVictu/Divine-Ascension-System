"""Emotional state representation for divine agents."""

from dataclasses import dataclass


@dataclass
class EmotionalState:
    """Simple container for emotion name and intensity."""

    name: str
    intensity: float = 0.0

