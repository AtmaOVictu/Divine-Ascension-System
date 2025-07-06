class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_name: str | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def set_emotion(self, name: str, intensity: float) -> None:
        """Set emotional state and adjust tension."""
        self.emotion_name = name
        self.update_emotion(intensity)

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
        emotion_prefix = (
            f"S c\u030custvom {self.emotion_name}: " if self.emotion_name else ""
        )
        if self.state == "Ego":
            return emotion_prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return emotion_prefix + "Resnica je relativna, oblikovana z nasimi odnosi."
        return emotion_prefix + "Vse resnice so eno, medsebojno povezane."
