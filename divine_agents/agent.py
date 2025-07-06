from dataclasses import dataclass, field
from typing import List


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTIONS = {"fear", "joy", "anger", "neutral"}

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history: List[str] = [state]

    def update_emotion(self, emotion_type: str, value: float) -> None:
        """Update emotion type and intensity, adjusting tension."""
        if emotion_type not in self.EMOTIONS:
            raise ValueError(f"Unknown emotion: {emotion_type}")
        self.emotion_type = emotion_type
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
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
        """Return a philosophical answer reflecting the current state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        emotion_map = {
            "fear": "Čutim strah.",
            "joy": "Občutim radost.",
            "anger": "Čutim jezo.",
            "neutral": ""
        }
        emotion_part = emotion_map.get(self.emotion_type, "")
        return f"{base} {emotion_part}".strip()
