"""Simple memory system for tracking agent state history."""

from __future__ import annotations

from typing import List


class MemorySystem:
    """Tracks historical states and transition types for an agent."""

    def __init__(self) -> None:
        self.history: List[str] = []
        self.current_state: str | None = None
        self.transition_points: List[str] = []

    def update(self, new_state: str, transition_type: str = "linear") -> None:
        """Save a new state and record the transition type."""
        if self.current_state is not None:
            self.history.append(self.current_state)
            self.transition_points.append(transition_type)
        self.current_state = new_state

    def revert(self) -> str | None:
        """Revert to the previous state if possible."""
        if self.history:
            self.current_state = self.history.pop()
            self.transition_points.pop()
            return self.current_state
        return None

    def get_all_history(self) -> List[str]:
        """Return a copy of the state history."""
        return list(self.history)

    def get_all_transitions(self) -> List[str]:
        """Return all recorded transition types."""
        return list(self.transition_points)

