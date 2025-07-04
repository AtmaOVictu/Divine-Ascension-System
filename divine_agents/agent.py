from dataclasses import dataclass
from typing import Union


@dataclass
class Emotion:
    """Represents the E/M/O/T/I0N structure of an emotion."""

    energy: float = 0.0
    motivation: float = 0.0
    feeling: float = 0.0
    tension: float = 0.0
    intensity: float = 0.0
    potential: float = 0.0

    def level(self) -> float:
        """Return averaged emotional level for transition checks."""
        return (
            self.energy
            + self.motivation
            + self.feeling
            + self.tension
            + self.intensity
            + self.potential
        ) / 6


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: Union[float, Emotion] = 0.0,
    ):
        self.name = name
        self.state = state
        self.tension = tension
        if isinstance(emotion, Emotion):
            self.emotion = emotion
            self.emotion_level = emotion.level()
        else:
            self.emotion = Emotion(intensity=float(emotion))
            self.emotion_level = float(emotion)
        self.history = [state]

    def update_emotion(self, value: Union[float, Emotion]) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        if isinstance(value, Emotion):
            self.emotion = value
            self.emotion_level = value.level()
        else:
            self.emotion.intensity = float(value)
            self.emotion_level = float(value)
        self.tension += self.emotion_level

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
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_level > 0.5:
            base += " Čutim intenzivna čustva."
        return base
