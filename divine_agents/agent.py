class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    #: Mapping of emotion type to tension influence factor
    EMOTION_TENSION = {
        "fear": 0.4,
        "anger": 0.5,
        "joy": -0.2,
        "sorrow": 0.3,
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_type: str = ""):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, emotion_type: str, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion_type = emotion_type
        self.emotion = value
        influence = self.EMOTION_TENSION.get(emotion_type, 0.0)
        self.tension += value * influence

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
        """Return a philosophical answer depending on the current state and emotion."""
        prefix = ""
        if self.emotion > 0.5:
            if self.emotion_type == "anger":
                prefix = "Z jezo pravim: "
            elif self.emotion_type == "fear":
                prefix = "S strahom povem: "
            elif self.emotion_type == "joy":
                prefix = "Z veseljem povem: "
            elif self.emotion_type == "sorrow":
                prefix = "Z žalostjo pravim: "

        if self.state == "Ego":
            msg = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            msg = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            msg = "Vse resnice so eno, medsebojno povezane."

        return prefix + msg
