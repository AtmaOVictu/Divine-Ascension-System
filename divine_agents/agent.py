class Agent:
    """Represent an ontological agent capable of emotional state transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTIONS = {
        "fear": 0.6,
        "joy": 0.3,
        "anger": 0.7,
        "neutral": 0.0,
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_label = emotion
        self.emotion = self.EMOTIONS.get(emotion, 0.0)
        self.history = [state]

    def update_emotion(self, value: str) -> None:
        """Update emotion label and adjust internal numeric intensity."""
        # Accept either a named emotion or direct numeric value
        if isinstance(value, str):
            self.emotion_label = value
            self.emotion = self.EMOTIONS.get(value, 0.0)
        else:
            self.emotion_label = "neutral"
            self.emotion = float(value)
        self.tension += self.emotion

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
        prefix = ""
        if self.emotion_label != "neutral":
            prefix = f"With {self.emotion_label}: "

        if self.state == "Ego":
            core = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            core = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            core = "Vse resnice so eno, medsebojno povezane."
        return prefix + core
