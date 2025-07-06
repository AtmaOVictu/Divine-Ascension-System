from __future__ import annotations

"""Ontological agent model with change logging."""

from typing import Any

from .logger import ChangeLogger


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, logger: ChangeLogger | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.logger = logger or ChangeLogger()
        self.logger.log_change(
            "init",
            f"Agent {self.name} initialized",
            {"state": self.state, "tension": self.tension, "emotion": self.emotion},
        )

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.logger.log_change(
            "emotion",
            f"{self.name} updated emotion to {value}",
            {"emotion": value, "tension": self.tension},
        )

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.logger.log_change(
            "tension",
            f"{self.name} updated tension to {value}",
            {"tension": value},
        )

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        previous = self.state
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        if previous != self.state:
            self.logger.log_change(
                "state_transition",
                f"{self.name} transitioned from {previous} to {self.state}",
                {"from": previous, "to": self.state},
            )
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            answer = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            answer = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            answer = "Vse resnice so eno, medsebojno povezane."
        self.logger.log_change(
            "response",
            f"{self.name} responded from state {self.state}",
            {"question": question, "answer": answer},
        )
        return answer
