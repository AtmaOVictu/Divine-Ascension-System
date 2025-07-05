class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral") -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str = "neutral") -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.emotion_type = emotion_type
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
        """Return a philosophical answer depending on the current state and emotion."""
        emotion_prefix = {
            "fear": "V strahu trdim, da ",
            "joy": "Z veseljem povem, da ",
            "anger": "Z jezo verjamem, da ",
        }.get(self.emotion_type, "Menim, da ")

        if self.state == "Ego":
            statement = "resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            statement = "resnica je relativna, oblikovana z našimi odnosi."
        else:
            statement = "vse resnice so eno, medsebojno povezane."
        return emotion_prefix + statement
