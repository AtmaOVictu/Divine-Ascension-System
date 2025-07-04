"""Core primitives for the dynamic agent system."""

from enum import Enum


class Emotion(Enum):
    """Basic emotional states that influence tension."""

    FEAR = "fear"
    JOY = "joy"
    ANGER = "anger"


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 current_emotion: Emotion | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.current_emotion = current_emotion
        self.history = [state]

    def update_emotion(self, emotion: Emotion, intensity: float) -> None:
        """Update emotional state and adjust tension accordingly."""
        self.current_emotion = emotion
        self.emotion = intensity
        self.tension += intensity

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
        emotion_note = (
            f" ({self.current_emotion.value})" if self.current_emotion else ""
        )
        if self.state == "Ego":
            return (
                "Resnica je absolutna in neodvisna od drugih." + emotion_note
            )
        if self.state == "Jaz":
            return (
                "Resnica je relativna, oblikovana z našimi odnosi." + emotion_note
            )
        return "Vse resnice so eno, medsebojno povezane." + emotion_note
