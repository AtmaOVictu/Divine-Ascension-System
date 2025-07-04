from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: List[str] = field(init=False)

    def __post_init__(self) -> None:
        self._validate_range(self.tension, "tension")
        self._validate_range(self.emotion, "emotion")
        self.history = [self.state]

    @staticmethod
    def _validate_range(value: float, field_name: str) -> None:
        if not 0.0 <= value <= 1.0:
            raise ValueError(f"{field_name} must be between 0 and 1")

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self._validate_range(value, "emotion")
        self.emotion = value
        new_tension = self.tension + value
        self.tension = min(1.0, max(0.0, new_tension))

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self._validate_range(value, "tension")
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
