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

    def update_emotion(self, value: float, kind: str = "neutral") -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.emotion_type = kind
        self.tension += value

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
        emotion_note = ""
        if self.emotion_type == "fear":
            emotion_note = "Čutim strah, zato "
        elif self.emotion_type == "anger":
            emotion_note = "Z jezo trdim, da "
        elif self.emotion_type == "joy":
            emotion_note = "V veselju menim, da "

        if self.state == "Ego":
            message = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            message = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            message = "Vse resnice so eno, medsebojno povezane."
        return f"{emotion_note}{message}"
