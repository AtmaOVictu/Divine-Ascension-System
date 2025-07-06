
"""Ontology driven agent implementation."""

from __future__ import annotations




EMOTION_INTENSITY = {
    "fear": 0.6,
    "anger": 0.7,
    "joy": 0.4,
    "sorrow": 0.5,
}


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label: str | None = None
        self.history = [state]

    def update_emotion(self, value: float, label: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        if label is not None:
            self.emotion_label = label

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def feel(self, emotion: str) -> None:
        """Experience a named emotion and adjust tension."""
        intensity = EMOTION_INTENSITY.get(emotion, 0.0)
        self.update_emotion(intensity, emotion)

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
        if self.emotion_label:
            return f"({self.emotion_label}) {base}"
        return base
