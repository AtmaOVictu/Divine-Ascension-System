from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from .emotion import Emotion


@dataclass
class Agent:
    """Ontological agent capable of transitioning states based on emotion and tension."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion_level: float = 0.0
    emotion_type: Emotion = Emotion.NEUTRAL
    history: List[str] = field(default_factory=list)

    STATES = ("Ego", "Jaz", "Enotnost")

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def update_emotion(self, emotion: Emotion, value: float) -> None:
        """Update emotion and adjust tension accordingly."""
        self.emotion_type = emotion
        self.emotion_level = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state and emotion."""
        emotion_prefix = {
            Emotion.FEAR: "Z občutkom strahu, ",
            Emotion.JOY: "Z občutkom veselja, ",
            Emotion.ANGER: "Z občutkom jeze, ",
        }.get(self.emotion_type, "")

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{emotion_prefix}{base}"
