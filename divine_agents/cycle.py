"""Ouroboros cycle utilities for ontological agents."""

from typing import List


class OuroborosCycle:
    """Represent a repeating cycle through ontological states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, start_state: str = "Ego") -> None:
        if start_state not in self.STATES:
            raise ValueError(f"Invalid start state: {start_state}")
        self.state = start_state
        self.history: List[str] = [start_state]

    def cycle(self) -> str:
        """Advance to the next state in the ouroboros sequence."""
        if self.state == "Ego":
            self.state = "Jaz"
        elif self.state == "Jaz":
            self.state = "Enotnost"
        else:
            self.state = "Ego"
        self.history.append(self.state)
        return self.state

    def run_cycles(self, n: int) -> List[str]:
        """Run ``n`` cycles and return the full history."""
        for _ in range(n):
            self.cycle()
        return self.history
