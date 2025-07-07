"""Ontological agents and state transition logic."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


DEFAULT_TRANSITION_MATRIX = [
    [0.7, 0.3, 0.0],
    [0.1, 0.3, 0.6],
    [0.0, 0.4, 0.6],
]


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_name: str = "neutral"
    history: List[str] = field(default_factory=lambda: ["Ego"])

    transition_matrix: List[List[float]] = field(default_factory=lambda: DEFAULT_TRANSITION_MATRIX)

    def update_emotion(self, value: float, name: str = "neutral") -> None:
        """Update emotion intensity, name and adjust tension accordingly."""
        self.emotion = value
        self.emotion_name = name
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self, use_matrix: bool = False) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if use_matrix:
                idx = self.STATES.index(self.state)
                row = self.transition_matrix[idx]
                max_idx = row.index(max(row))
                self.state = self.STATES[max_idx]
            else:
                if self.state == "Ego":
                    self.state = "Jaz"
                elif self.state == "Jaz":
                    self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"[{self.emotion_name}] {base}"
