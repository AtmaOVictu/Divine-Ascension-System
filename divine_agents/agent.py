from dataclasses import dataclass, field
from typing import List


class Emotion:
    """Simple container for emotion type and intensity."""

    def __init__(self, kind: str = "neutral", intensity: float = 0.0) -> None:
        self.kind = kind
        self.intensity = intensity

    def update(self, kind: str, intensity: float) -> None:
        self.kind = kind
        self.intensity = intensity


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: Emotion | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion or Emotion()
        self.history: List[str] = [state]

    def update_emotion(self, kind: str, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion.update(kind, value)
        self.tension += value

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
        emotion_prefix = (
            f"[{self.emotion.kind.upper()}({self.emotion.intensity:.1f})] "
            if self.emotion.kind != "neutral" else ""
        )

        if self.state == "Ego":
            return emotion_prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return emotion_prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return emotion_prefix + "Vse resnice so eno, medsebojno povezane."
