from typing import Optional

from .logger import ChangeLogger


class Agent:
    """Ontological agent capable of transitioning through philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, logger: Optional[ChangeLogger] = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.logger = logger or ChangeLogger()
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.logger.log(
            "emotion",
            f"Emotion updated to {value}",
            {"emotion": value, "tension": self.tension},
        )

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.logger.log(
            "tension",
            f"Tension updated to {value}",
            {"tension": value},
        )

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            self.logger.log(
                "state_transition",
                f"Transitioned to {self.state}",
                {"state": self.state},
            )
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by current state and emotion."""
        if self.state == "Ego":
            reply = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            reply = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            reply = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            reply += " Čustva močno vplivajo na moje dojemanje."
        return reply

    def interact(self, other: "Agent") -> None:
        """Record interaction with another agent."""
        self.logger.log(
            "interaction",
            f"Interacted with {other.name}",
            {"partner": other.name},
        )
