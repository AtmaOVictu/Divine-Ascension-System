"""Core classes for the divine agent system."""

from dataclasses import dataclass, field
from typing import List


class Agent:
    """Ontological agent capable of emotional and state transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        if state not in self.STATES:
            raise ValueError(f"Unknown state '{state}'")
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history: List[str] = [state]

    def update_emotion(self, delta: float) -> None:
        """Increase emotion and adjust tension accordingly."""
        self.emotion = max(0.0, min(1.0, self.emotion + delta))
        self.tension = max(0.0, min(1.0, self.tension + delta))

    def update_tension(self, value: float) -> None:
        """Directly set the tension level (0..1)."""
        self.tension = max(0.0, min(1.0, value))

    def _should_transition(self) -> bool:
        """Determine whether thresholds for state change are met."""
        return self.tension > 0.7 or self.emotion > 0.5

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self._should_transition():
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            return f"{base} Čutim to zelo močno."  # emotional emphasis
        return base
