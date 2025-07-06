class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        if emotion_type is not None:
            self.emotion_type = emotion_type
        self.tension += value

    def set_emotion(self, emotion_type: str, value: float) -> None:
        """Convenience wrapper to set emotion and emotion type."""
        self.update_emotion(value, emotion_type)

    def _emotion_phrase(self) -> str:
        """Return a phrase reflecting current emotional state."""
        if self.emotion_type == "fear":
            return " Čutim strah." if self.emotion > 0 else ""
        if self.emotion_type == "joy":
            return " Občutim veselje." if self.emotion > 0 else ""
        if self.emotion_type == "anger":
            return " Preveva me jeza." if self.emotion > 0 else ""
        return ""

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
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return base + self._emotion_phrase()
