from dataclasses import dataclass, field
from enum import Enum
from typing import List


class Emotion(Enum):
    """Basic emotional categories influencing agent behaviour."""

    FEAR = "fear"
    JOY = "joy"
    ANGER = "anger"
    NEUTRAL = "neutral"


@dataclass
class Agent:
    """Ontological agent capable of transitioning states based on tension and emotion."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_type: Emotion = Emotion.NEUTRAL
    history: List[str] = field(default_factory=lambda: ["Ego"])

    def update_emotion(self, value: float, kind: Emotion = Emotion.NEUTRAL) -> None:
        """Update emotion intensity, emotion type and adjust tension accordingly."""
        self.emotion = max(0.0, min(1.0, value))
        self.emotion_type = kind
        self.tension = min(1.0, self.tension + self.emotion)

    def update_tension(self, value: float) -> None:
        """Directly set tension level within [0, 1]."""
        self.tension = max(0.0, min(1.0, value))

    def transition(self) -> str:
        """Perform state transition when thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        prefix = ""
        if self.emotion_type != Emotion.NEUTRAL:
            prefix = f"[{self.emotion_type.value}] "

        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."
