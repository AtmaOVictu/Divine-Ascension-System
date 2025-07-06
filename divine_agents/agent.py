class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_label: str = "neutral",
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    def update_emotion(self, value: float, label: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        if label is not None:
            self.emotion_label = label
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
        emotional_prefix = ""
        if self.emotion_label == "fear":
            emotional_prefix = "(s strahom) "
        elif self.emotion_label == "joy":
            emotional_prefix = "(z veseljem) "
        elif self.emotion_label == "anger":
            emotional_prefix = "(z jezo) "

        if self.state == "Ego":
            truth = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            truth = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            truth = "Vse resnice so eno, medsebojno povezane."

        return f"{emotional_prefix}{truth}"
