from dataclasses import dataclass


@dataclass
class EmotionalState:
    """Represents the current emotional state of an agent."""

    label: str = "neutral"
    intensity: float = 0.0


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float | None = None, emotion_label: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        if emotion is None:
            emotion = 0.0
        self.emotion = EmotionalState(emotion_label, emotion)
        self.history = [state]

    def update_emotion(self, value: float, label: str | None = None) -> None:
        """Update emotion intensity and optionally set emotion label."""
        self.emotion.intensity = value
        if label is not None:
            self.emotion.label = label
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
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]
        if self.emotion.intensity > 0.5 and self.emotion.label != "neutral":
            return f"({self.emotion.label}) {base}"
        return base
