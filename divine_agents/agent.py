from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion_level: float = 0.0
    emotion_type: str = "neutral"
    history: List[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")
    THRESHOLD_TENSION = 0.7
    THRESHOLD_EMOTION = 0.5

    def update_emotion(self, e_type: str, value: float) -> None:
        """Update emotion intensity and type, adjusting tension."""
        self.emotion_type = e_type
        self.emotion_level = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > self.THRESHOLD_TENSION or self.emotion_level > self.THRESHOLD_EMOTION:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]
        if self.emotion_type != "neutral":
            return f"Z občutkom {self.emotion_type} odgovarja: {base}"
        return base
