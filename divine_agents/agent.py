from dataclasses import dataclass


@dataclass
class Emotion:
    """Represents an emotion with a name and intensity."""

    name: str
    level: float


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: Emotion | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion: Emotion | None = emotion
        self.history = [state]

    def update_emotion(self, name: str, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = Emotion(name, value)
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        level = self.emotion.level if self.emotion else 0.0
        if self.tension > 0.7 or level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state and emotion."""
        emotion_note = f" Čutim {self.emotion.name}." if self.emotion else ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return base + emotion_note
