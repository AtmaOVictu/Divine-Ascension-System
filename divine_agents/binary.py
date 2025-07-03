from __future__ import annotations

"""Binary agent module implementing simple 0/1 state interactions."""

from dataclasses import dataclass


@dataclass
class BinaryAgent:
    """Represents a simplified agent with binary states 0 (stable) or 1 (active)."""

    name: str
    state: int = 0

    def interact(self, other: "BinaryAgent") -> tuple[int, int]:
        """Interact with another agent.

        If both agents are in state 0, the interaction activates them (state 1).
        Returns the resulting states for convenience.
        """
        if self.state == 0 and other.state == 0:
            self.state = other.state = 1
        return self.state, other.state

    def __repr__(self) -> str:  # pragma: no cover - simple debug helper
        return f"BinaryAgent(name={self.name!r}, state={self.state})"
