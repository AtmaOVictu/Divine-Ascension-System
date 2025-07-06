from typing import Optional, Dict

from .logger import ChangeLogger


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 log_file: str = "change_log.json"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.logger = ChangeLogger(log_file)

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.logger.log_change(
            "emotion",
            f"Posodobitev čustva: {value}",
            {"emotion": value, "tension": self.tension},
        )

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.logger.log_change(
            "tension",
            f"Posodobitev napetosti: {value}",
            {"tension": value},
        )

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            previous = self.state
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            if previous != self.state:
                self.logger.log_change(
                    "state_transition",
                    f"Prehod iz {previous} v {self.state}",
                    {"from": previous, "to": self.state},
                )
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

        if self.emotion > 0.5:
            return f"{base} (Čustveni odziv: {self.emotion:.1f})"
        return base
