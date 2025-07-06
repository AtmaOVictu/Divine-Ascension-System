class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTIONS = ("neutral", "fear", "anger", "joy")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion_value: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_value = emotion_value
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, emotion_type: str, value: float) -> None:
        """Update emotion type and intensity, adjusting tension."""
        assert 0.0 <= value <= 1.0, "Emotion value must be within [0, 1]"
        self.emotion_type = emotion_type
        self.emotion_value = value
        if emotion_type in ("fear", "anger"):
            self.tension = min(1.0, self.tension + value)
        elif emotion_type == "joy":
            self.tension = max(0.0, self.tension - value / 2)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        assert 0.0 <= value <= 1.0, "Tension must be within [0, 1]"
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_value > 0.5:
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

        if self.emotion_type == "anger":
            base += " Čutim jezo, kar povečuje napetost."
        elif self.emotion_type == "fear":
            base += " Preveva me strah pred zmoto."
        elif self.emotion_type == "joy":
            base += " To me navdaja z veseljem."
        return base
