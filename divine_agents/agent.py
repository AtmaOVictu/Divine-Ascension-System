"""Core logic for ontological agents."""

from __future__ import annotations

from typing import List

from .krak import Krak


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history: List[str] = [state]
        self.kraks: List[Krak] = []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def add_krak(self, krak: Krak) -> None:
        """Register a Krak task with the agent."""
        self.kraks.append(krak)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self._activate_kraks()
        self.history.append(self.state)
        return self.state

    def __repr__(self) -> str:  # pragma: no cover - simple debug helper
        return f"Agent(name={self.name}, state={self.state}, tension={self.tension}, emotion={self.emotion})"

    def _activate_kraks(self) -> None:
        """Activate all kraks whose conditions are satisfied."""
        for krak in self.kraks:
            krak.check_and_activate(self)

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on current state and emotion."""
        base = ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} (emocija: {self.emotion:.1f})"
