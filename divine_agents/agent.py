from __future__ import annotations

from .emotions import EmotionType, EMOTION_TENSION_FACTOR


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion_level: float = 0.0,
        emotion: EmotionType = EmotionType.NEUTRAL,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_level = emotion_level
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, emotion: EmotionType, level: float) -> None:
        """Update emotion type and intensity, adjusting tension accordingly."""
        self.emotion = emotion
        self.emotion_level = level
        self.tension += level * EMOTION_TENSION_FACTOR.get(emotion, 0.0)

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
        """Return a philosophical answer depending on the current state."""
        state_philosophy = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }
        emotion_suffix = {
            EmotionType.NEUTRAL: "",
            EmotionType.FEAR: " (v strahu)",
            EmotionType.JOY: " (z radostjo)",
            EmotionType.ANGER: " (v jezi)",
        }[self.emotion]
        return state_philosophy[self.state] + emotion_suffix
