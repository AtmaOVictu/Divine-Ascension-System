"""Core agent logic for the ontological system."""

from typing import Dict


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0) -> None:
        self.name: str = name
        self.state: str = state
        self.tension: float = tension
        self.emotion: float = emotion
        self.history: list[str] = [state]

    EMOTION_EFFECTS: Dict[str, float] = {
        "fear": 1.0,
        "anger": 0.8,
        "joy": -0.4,
    }

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def apply_emotion(self, emotion: str, intensity: float) -> None:
        """Influence tension using a named emotion."""
        self.emotion = intensity
        effect = self.EMOTION_EFFECTS.get(emotion, 0.0)
        self.tension += effect * intensity

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
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
