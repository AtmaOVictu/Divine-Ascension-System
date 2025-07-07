class Agent:
    """Represent an ontological agent capable of transitioning states.

    The agent tracks its current ontological ``state`` together with an
    ``emotion`` value and associated ``tension``.  Transitions are triggered
    whenever the tension exceeds ``0.7`` or the emotion is stronger than
    ``0.5`` as required by the specification.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_label: str | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label or ""
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def set_emotion(self, label: str, value: float) -> None:
        """Assign a named emotion and adjust tension."""
        self.emotion_label = label
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
        if self.state == "Ego":
            message = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            message = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            message = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_label == "fear":
            message += " Čutim strah."
        elif self.emotion_label == "joy":
            message += " Čutim veselje."
        elif self.emotion_label == "anger":
            message += " Čutim jezo."

        return message
