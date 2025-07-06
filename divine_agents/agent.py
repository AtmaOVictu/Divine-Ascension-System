"""Ontological agent implementation."""

from dataclasses import dataclass


@dataclass
class Emotion:
    """Simple container representing an emotion and its intensity."""

    kind: str = "neutral"
    intensity: float = 0.0


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: Emotion | None = None):
        self.name = name
        self.state = state
        self.tension = float(tension)
        self.emotion: Emotion = emotion if emotion else Emotion()
        self.history = [state]

    def set_emotion(self, kind: str, intensity: float) -> None:
        """Set the agent's emotion and adjust tension."""
        self.emotion.kind = kind
        self.emotion.intensity = intensity
        self.tension += intensity

    def update_emotion(self, intensity: float) -> None:
        """Update only emotion intensity and adjust tension."""
        self.emotion.intensity = intensity
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
        """Return a philosophical answer depending on the current state and emotion."""
        prefix_map = {
            "anger": "Z jezo povem, da ",
            "fear": "S strahom povem, da ",
            "joy": "Z veseljem povem, da ",
            "sorrow": "Žalostno izrečem, da ",
        }
        prefix = prefix_map.get(self.emotion.kind, "") if self.emotion.intensity > 0 else ""

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return prefix + base
