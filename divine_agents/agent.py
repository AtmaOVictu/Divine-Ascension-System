from dataclasses import dataclass


@dataclass
class Emotion:
    """Represents an emotional state with a type and intensity."""

    kind: str = "neutral"
    intensity: float = 0.0


class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: Emotion | None = None):
        self.name = name
        self.state = state
        self.tension = float(tension)
        self.emotion = emotion or Emotion()
        self.history = [state]

    # ------------------------------------------------------------------
    # State and emotion management
    # ------------------------------------------------------------------
    def set_emotion(self, kind: str, intensity: float) -> None:
        """Set emotion and update tension accordingly."""
        self.emotion = Emotion(kind, intensity)
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = float(value)

    def transition(self) -> str:
        """Transition to the next state if thresholds are met."""
        if self.tension > 0.7 or self.emotion.intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    # ------------------------------------------------------------------
    # Dialogue helpers
    # ------------------------------------------------------------------
    def respond(self, question: str) -> str:
        """Return a philosophical answer based on current state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z nasimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion.kind != "neutral":
            base += f" Čutim {self.emotion.kind}."
        return base
