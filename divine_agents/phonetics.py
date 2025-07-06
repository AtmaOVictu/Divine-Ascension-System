"""Phonetic sound processing utilities."""

from typing import Dict, Tuple

from .agent import Agent

# Map phonetic sounds to adjustments on emotion or tension
PHONETIC_TRUTH_MAP: Dict[str, Tuple[str, float]] = {
    "ba": ("emotion", 0.6),  # promotes positive emotion leading to transition
    "ka": ("tension", 0.8),  # negation adds tension
    "ra": ("emotion", 0.4),  # wisdom but below threshold
}


def process_sound(agent: Agent, sound: str) -> str:
    """Apply a phonetic sound to an agent and return the new state."""
    effect = PHONETIC_TRUTH_MAP.get(sound)
    if effect:
        kind, value = effect
        if kind == "emotion":
            agent.update_emotion(value)
        elif kind == "tension":
            agent.update_tension(value)
    return agent.transition()
