"""Agent definitions and logic for ontological transitions."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_label: str = "neutral"
    history: List[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")

    def update_emotion(self, label: str, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion_label = label
        self.emotion = value
        if label in {"fear", "angry"}:
            self.tension += value
        elif label in {"joy", "happy"}:
            self.tension = max(0.0, self.tension - value)
        else:
            self.tension += value * 0.1

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
        """Return a philosophical answer depending on the current state."""
        base = ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        if self.emotion_label in {"fear", "angry"}:
            return f"{base} Občutim {self.emotion_label}."
        if self.emotion_label in {"joy", "happy"}:
            return f"{base} Občutim {self.emotion_label}."
        return base
