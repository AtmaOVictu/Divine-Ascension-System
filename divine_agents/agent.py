"""Ontological agent model with emotional transitions."""
from dataclasses import dataclass, field
from typing import List


@dataclass
class Emotion:
    """Simple emotion container."""
    name: str = "neutral"
    intensity: float = 0.0


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: Emotion = field(default_factory=Emotion)
    history: List[str] = field(default_factory=list)

    STATES = ("Ego", "Jaz", "Enotnost")

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def update_emotion(self, name: str, intensity: float) -> None:
        """Update emotion and adjust tension."""
        self.emotion = Emotion(name, intensity)
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion.intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        emotion_prefix = {
            "fear": "S strahom ",
            "anger": "Z jezo ",
            "joy": "Z veseljem ",
        }.get(self.emotion.name, "")

        if self.state == "Ego":
            answer = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            answer = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            answer = "Vse resnice so eno, medsebojno povezane."

        return f"{emotion_prefix}{answer}"
