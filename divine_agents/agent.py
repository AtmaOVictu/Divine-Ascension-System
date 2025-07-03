class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        The name of the agent.
    state:
        Ontological state (``"Ego"``, ``"Jaz"`` or ``"Enotnost"``).
    tension:
        Current tension level influencing transitions.
    emotion:
        Intensity of the current emotion influencing transitions.
    emotion_type:
        Descriptive label of the current emotion (e.g. ``"fear"``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_type: str | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type or ""
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and optionally set the emotion type.

        Parameters
        ----------
        value:
            Intensity of the emotion.
        emotion_type:
            Label describing the emotion (e.g. ``"fear"``).
        """
        self.emotion = value
        if emotion_type:
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
        """Return a philosophical answer depending on the current state.

        The current emotional label is appended to emphasise how feelings
        influence the response.
        """
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_type:
            base += f" (čustvo: {self.emotion_type})"
        return base
