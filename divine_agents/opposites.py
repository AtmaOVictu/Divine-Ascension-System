"""Ontological opposites generator.

This module provides a simple generator that yields pairs of opposing
concepts. It can also create textual transitions between a state and
its opposite.
"""
from __future__ import annotations

import random
from typing import Dict, Tuple


class OntologicalOppositesGenerator:
    """Generate ontological opposites and transitions between them."""

    def __init__(self) -> None:
        self.opposites: Dict[str, str] = {
            "biti": "ničnost",
            "tišina": "zven",
            "ego": "jaz",
            "resnica": "laž",
            "svetloba": "tema",
            "umirjenost": "jeza",
            "vednost": "nevednost",
        }

    def generate_opposites(self) -> Tuple[str, str]:
        """Return a random pair of opposites."""
        return random.choice(list(self.opposites.items()))

    def get_opposite(self, state: str) -> str | None:
        """Get the opposite of a given state if known."""
        return self.opposites.get(state)

    def create_transition(self, state: str) -> str:
        """Return a textual description of the transition to the opposite."""
        opposite = self.get_opposite(state)
        if opposite:
            return f"Prehod iz {state} v {opposite}."
        return f"Nema nasprotja za {state}."

__all__ = ["OntologicalOppositesGenerator"]
