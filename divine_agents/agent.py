class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 emotional_state: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotional_state = emotional_state
        self.history = [state]

    def update_emotion(self, value: float, emotion_name: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value: float
            Intensity of the current emotion.
        emotion_name: str | None
            Optional textual representation of the emotion (e.g. "joy", "anger").
        """
        self.emotion = value
        if emotion_name is not None:
            self.emotional_state = emotion_name
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
        """Return a philosophical answer influenced by current state and emotion."""
        prefix = ""
        if self.emotional_state == "joy":
            prefix = "Veselo povem: "
        elif self.emotional_state == "anger":
            prefix = "Z jezo povem: "
        elif self.emotional_state == "fear":
            prefix = "S strahom povem: "

        if self.state == "Ego":
            statement = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            statement = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            statement = "Vse resnice so eno, medsebojno povezane."
        return f"{prefix}{statement}".strip()
