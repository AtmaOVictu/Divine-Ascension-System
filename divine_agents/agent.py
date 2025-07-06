"""Core agent logic for the Divine Ascension system."""

from typing import Dict


EMOTION_INTENSITY: Dict[str, float] = {
    "neutral": 0.0,
    "joy": 0.4,
    "fear": 0.6,
    "anger": 0.7,
}


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_name: str = "neutral",
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def set_emotion(self, emotion: str) -> None:
        """Set emotion by name and adjust internal values."""
        self.emotion_name = emotion
        intensity = EMOTION_INTENSITY.get(emotion, 0.0)
        self.update_emotion(intensity)

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
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_name == "fear":
            base += " Občutim strah."
        elif self.emotion_name == "anger":
            base += " Jezen sem."
        elif self.emotion_name == "joy":
            base += " Veselim se."

        return base

    def speak(self) -> str:
        """Return formatted statement with current state and emotion."""
        response = self.respond("Kaj je resnica?")
        return f"{self.name} ({self.state}, {self.emotion_name}): {response}"
