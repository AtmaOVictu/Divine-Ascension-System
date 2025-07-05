"""Oracle agent with memory of transitions."""
from typing import Dict, List

from .agent import Agent


class OracleAgent(Agent):
    """Agent that records transitions and can suggest future moves."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.transitions: List[Dict[str, str]] = []

    def record_transition(self, from_state: str, to_state: str) -> None:
        """Store a transition from one state to another."""
        self.transitions.append({"from": from_state, "to": to_state})

    def transition(self) -> str:
        """Override to record state changes."""
        previous = self.state
        new_state = super().transition()
        if previous != new_state:
            self.record_transition(previous, new_state)
        return new_state

    def suggest_next_step(self, current_state: str) -> List[str]:
        """Return possible next states seen after the given state."""
        return [t["to"] for t in self.transitions if t["from"] == current_state]

    def predict_future(self) -> str | None:
        """Predict the next state based on the last transition."""
        if not self.transitions:
            return None
        last = self.transitions[-1]
        return last["to"]
