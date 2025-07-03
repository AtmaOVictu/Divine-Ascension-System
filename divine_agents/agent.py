from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Ontological agent capable of emotional state transitions."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion_level: float = 0.0
    emotion_label: str = "neutral"
    history: List[str] = field(default_factory=lambda: ["Ego"])

    def update_emotion(self, level: float, label: str = "neutral") -> None:
        """Update emotion level and label while increasing tension."""
        self.emotion_level = level
        self.emotion_label = label
        self.tension += level

    def update_tension(self, value: float) -> None:
        """Set tension directly."""
        self.tension = value

    def transition(self) -> str:
        """Transition between states if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical response influenced by state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_label != "neutral":
            return f"({self.emotion_label}) {base}"
        return base
