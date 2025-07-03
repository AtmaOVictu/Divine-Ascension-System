from dataclasses import dataclass


@dataclass
class Emotion:
    """Represents the emotional state of an agent."""

    type: str = "neutral"
    intensity: float = 0.0


class Agent:
    """Ontological agent capable of philosophical state transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0, emotion: Emotion | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion or Emotion()
        self.history = [state]

    def update_emotion(self, emotion_type: str, intensity: float) -> None:
        """Set emotion and adjust tension."""
        self.emotion.type = emotion_type
        self.emotion.intensity = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition if thresholds are exceeded."""
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
            f"V {self.emotion.type} čutim, da " if self.emotion.type != "neutral" else ""
        )
        if self.state == "Ego":
            return emotion_prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return emotion_prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return emotion_prefix + "Vse resnice so eno, medsebojno povezane."
