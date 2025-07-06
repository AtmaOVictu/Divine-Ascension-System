from dataclasses import dataclass


@dataclass
class Emotion:
    """Represents an emotional state with a type and intensity."""

    type: str = "neutral"
    intensity: float = 0.0


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: Emotion | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion or Emotion()
        self.history = [state]

    def update_emotion(self, emotion_type: str, intensity: float) -> None:
        """Update emotion state and adjust tension accordingly."""
        self.emotion.type = emotion_type
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

    def _emotion_prefix(self) -> str:
        if self.emotion.type == "fear":
            return "S strahom priznavam,"
        if self.emotion.type == "anger":
            return "Z jezo povem,"
        if self.emotion.type == "joy":
            return "Z veseljem delim,"
        return ""

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state with emotional nuance."""
        prefix = self._emotion_prefix()
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{prefix} {base}".strip()
