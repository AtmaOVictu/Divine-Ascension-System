"""Symbolic utilities for ontological transitions."""

from __future__ import annotations

# String constants representing symbolic variables
TENSION = 'τ'
EMOTION = 'ϵ'


def check_transition(tension: float, emotion: float) -> bool:
    """Return True if a transition should occur based on thresholds."""
    return tension > 0.7 or emotion > 0.5


def transition_symbol(tension: float, emotion: float) -> str:
    """Return the symbolic representation for a transition."""
    if check_transition(tension, emotion):
        return '⊕' if tension > emotion else '⊗'
    return ''
