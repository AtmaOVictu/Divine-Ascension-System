"""Symbolic utilities for ontological transitions."""

from __future__ import annotations

# Define symbolic variables as simple string representations. Using plain strings
# avoids the need for external dependencies such as ``sympy`` while still
# conveying the symbolic intent of the framework.
TENSION = 'τ'
EMOTION = 'ϵ'


def check_transition(tension: float, emotion: float) -> bool:
    """Return True if a state transition should occur."""
    return tension > 0.7 or emotion > 0.5


def transition_to_symbol(tension: float, emotion: float) -> str:
    """Convert numeric values into an ontological transition symbol."""
    if check_transition(tension, emotion):
        if tension > emotion:
            return "⊕ (Transcendence - Ego to Jaz)"
        else:
            return "⊗ (Balance - Jaz to Enotnost)"
    return "No transition, remains in current state"
