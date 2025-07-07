class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    #: influence of each emotion type on the tension level
    EMOTION_INFLUENCE = {
        "fear": 0.5,
        "anger": 0.6,
        "joy": -0.3,
        "sorrow": 0.4,
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = ""
        self.history = [state]

    def update_emotion(self, name: str, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion_name = name
        self.emotion = value
        self.tension += value * self.EMOTION_INFLUENCE.get(name, 0.0)

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

        tone = ""
        if self.emotion_name == "fear":
            tone = " Govorim s strahom."
        elif self.emotion_name == "anger":
            tone = " Govorim z jezo."
        elif self.emotion_name == "joy":
            tone = " Govorim z veseljem."
        elif self.emotion_name == "sorrow":
            tone = " Govorim z žalostjo."

        return f"{base}{tone}"
