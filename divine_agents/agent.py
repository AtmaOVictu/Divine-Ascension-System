class Agent:
    """Represent an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    #: mapping of emotion names to default intensity values
    EMOTION_EFFECT = {
        "fear": 0.6,
        "anger": 0.6,
        "joy": 0.4,
        "neutral": 0.2,
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_name: str = "neutral"):
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

    def set_emotion(self, name: str, value: float | None = None) -> None:
        """Set emotion type and intensity.

        If ``value`` is not provided, a default value defined in
        :data:`EMOTION_EFFECT` is used.
        """
        self.emotion_name = name
        if value is None:
            value = self.EMOTION_EFFECT.get(name, 0.2)
        self.update_emotion(value)

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
        if self.emotion_name == "anger":
            prefix = "Z jezo izjavljam, "
        elif self.emotion_name == "fear":
            prefix = "S strahom menim, "
        elif self.emotion_name == "joy":
            prefix = "Z veseljem povem, "
        else:
            prefix = ""

        if self.state == "Ego":
            answer = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            answer = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            answer = "Vse resnice so eno, medsebojno povezane."

        return prefix + answer
