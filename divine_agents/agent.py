from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Ontological agent capable of state transitions based on emotion and tension."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_name: str = "neutral"
    history: List[str] = field(default_factory=list)

    STATES = ("Ego", "Jaz", "Enotnost")

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def update_emotion(self, name: str, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion_name = name
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
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
        """Return a philosophical answer depending on the current ontological state."""
        prefix = ""
        if self.emotion_name != "neutral":
            prefix = f"{self.emotion_name.capitalize()}: "

        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."
