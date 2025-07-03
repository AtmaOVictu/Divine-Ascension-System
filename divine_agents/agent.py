from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto


class EmotionType(Enum):
    """Possible emotional states influencing an agent."""

    NEUTRAL = auto()
    FEAR = auto()
    JOY = auto()
    ANGER = auto()


@dataclass
class Agent:
    """Ontological agent capable of transitioning between states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_type: EmotionType = EmotionType.NEUTRAL
    history: list[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")

    def update_emotion(self, emotion_type: EmotionType, value: float) -> None:
        """Update emotion type and intensity, adjusting tension."""
        self.emotion_type = emotion_type
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
        """Return a philosophical answer influenced by state and emotion."""
        prefix = ""
        if self.emotion_type == EmotionType.FEAR:
            prefix = "S strahom povem: "
        elif self.emotion_type == EmotionType.JOY:
            prefix = "Z veseljem povem: "
        elif self.emotion_type == EmotionType.ANGER:
            prefix = "Z jezo povem: "

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return prefix + base
