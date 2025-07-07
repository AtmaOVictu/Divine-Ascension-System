from dataclasses import dataclass
from typing import List


@dataclass
class Emotion:
    """Represents an emotion with a type and intensity."""

    kind: str
    intensity: float = 0.0


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: Emotion | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion or Emotion("neutral", 0.0)
        self.history: List[str] = [state]

    def update_emotion(self, kind: str, intensity: float) -> None:
        """Update emotion with a new type and adjust tension accordingly."""
        self.emotion = Emotion(kind, intensity)
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
        """Return a philosophical answer influenced by the current state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        match self.emotion.kind:
            case "fear":
                mood = " Čutim strah pred spremembo."
            case "anger":
                mood = " Občutim jezo do nasprotnih pogledov."
            case "joy":
                mood = " Preveva me veselje ob razpravi."
            case _:
                mood = ""
        return base + mood
