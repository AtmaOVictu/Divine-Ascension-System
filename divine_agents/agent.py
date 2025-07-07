from dataclasses import dataclass


@dataclass
class Emotion:
    """Represents the emotional state of an agent."""

    name: str = "neutral"
    intensity: float = 0.0


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: Emotion | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion if emotion is not None else Emotion()
        self.history = [state]

    def update_emotion(self, name: str, intensity: float) -> None:
        """Update emotion type and intensity, adjusting tension accordingly."""
        self.emotion = Emotion(name, intensity)
        self.tension += intensity

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
        feeling = (
            f"ob občutku {self.emotion.name}" if self.emotion.name != "neutral" else "brez posebnih čustev"
        )

        if self.state == "Ego":
            return f"{feeling}, trdim, da je resnica absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return f"{feeling}, menim, da je resnica relativna, oblikovana z našimi odnosi."
        return f"{feeling}, vidim, da so vse resnice eno, medsebojno povezane."
