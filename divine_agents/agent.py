"""Core agent logic for the Divine-Ascension system."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """An ontological agent capable of emotion-driven state transitions."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: List[str] = field(default_factory=list)

    TRANSITION_TENSION_THRESHOLD: float = 0.7
    TRANSITION_EMOTION_THRESHOLD: float = 0.5

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def update_emotion(self, value: float) -> None:
        """Set emotion intensity and increase tension accordingly."""
        self.emotion = value
        self.tension += value

    def feel(self, value: float) -> None:
        """Convenience wrapper for updating emotion."""
        self.update_emotion(value)

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if (
            self.tension > self.TRANSITION_TENSION_THRESHOLD
            or self.emotion > self.TRANSITION_EMOTION_THRESHOLD
        ):
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

        if self.emotion > 0.7:
            return f"{base} Čutim to zelo močno."
        if self.emotion > 0.3:
            return f"{base} To me gane."
        return base
