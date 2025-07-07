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
        if emotion_type is not None:
            self.emotion_type = emotion_type
        self.emotion = value
        self.tension = max(0.0, min(1.0, self.tension + value))

    def set_emotion(self, emotion_type: str, value: float) -> None:
        """Convenience method to set emotion type and intensity."""
        self.update_emotion(value, emotion_type)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, min(1.0, value))

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
        emotion_prefix = ""
        if self.emotion_type == "fear":
            emotion_prefix = "S strahom povem, da "
        elif self.emotion_type == "joy":
            emotion_prefix = "Z veseljem trdim, da "
        elif self.emotion_type == "anger":
            emotion_prefix = "Z jezo razlagam, da "

        if self.state == "Ego":
            return emotion_prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return emotion_prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return emotion_prefix + "Vse resnice so eno, medsebojno povezane."
