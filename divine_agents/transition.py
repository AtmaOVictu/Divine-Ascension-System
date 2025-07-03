"""Utility classes for logging transitions between states."""

from typing import List


class TransitionSystem:
    """Log transitions performed by agents."""

    def __init__(self) -> None:
        self._history: List[str] = []

    def log(self, agent_name: str, from_state: str, to_state: str) -> str:
        """Record a transition and return the log entry."""
        entry = f"{agent_name}: {from_state} -> {to_state}"
        self._history.append(entry)
        return entry

    @property
    def history(self) -> List[str]:
        """Return the stored transition history."""
        return list(self._history)
