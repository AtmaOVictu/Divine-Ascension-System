from dataclasses import dataclass


@dataclass
class Emotion:
    """Simple container to hold emotion type and intensity."""

    kind: str = "neutral"
    intensity: float = 0.0


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: Emotion | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion if emotion else Emotion()
        self.history = [state]
        self.stable_axis = "Enotnost"

    def update_emotion(self, kind: str, intensity: float) -> None:
        """Update emotion and adjust tension accordingly."""
        self.emotion = Emotion(kind, intensity)
        self.tension += intensity
        if kind == "fear" and self.state != self.stable_axis:
            # Fear may force the agent back to its stable axis
            self.state = self.stable_axis
            self.history.append(self.state)

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
        postfix = f" (emocija: {self.emotion.kind})"
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih." + postfix
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi." + postfix
        return "Vse resnice so eno, medsebojno povezane." + postfix
