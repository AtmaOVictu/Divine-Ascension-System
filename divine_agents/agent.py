"""Core agent logic for the ontological system."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: List[str] = field(default_factory=list)

    STATES = ("Ego", "Jaz", "Enotnost")

    def __post_init__(self) -> None:
        if not self.history:
            self.history.append(self.state)

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        # Emotion feeds into tension which may trigger transitions
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

    # ------------------------------------------------------------------
    # Dialogue helpers
    # ------------------------------------------------------------------
    def describe_emotion(self) -> str:
        """Return a short textual description of the current emotion level."""
        if self.emotion >= 0.8:
            return "intenzivno"
        if self.emotion >= 0.5:
            return "močno"
        return "mirno"

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        prefix = f"({self.describe_emotion()})"
        if self.state == "Ego":
            answer = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            answer = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            answer = "Vse resnice so eno, medsebojno povezane."
        return f"{prefix} {answer}"
