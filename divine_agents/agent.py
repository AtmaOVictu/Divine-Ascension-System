class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral") -> None:
        """Create a new agent.

        Parameters
        ----------
        name:
            Agent's identifier.
        state:
            Initial ontological state.
        tension:
            Internal tension value.
        emotion:
            Intensity of the current emotion in range ``[0, 1]``.
        emotion_type:
            Descriptor of the current emotion (e.g. ``"fear"`` or ``"joy"``).
        """
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            New emotional intensity in range ``[0, 1]``.
        emotion_type:
            Optional descriptor of the emotion. If ``None`` the previous
            ``emotion_type`` is preserved.
        """
        self.emotion = value
        if emotion_type is not None:
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

        The emotional type influences the tone of the response.
        """
        prefix = ""
        if self.emotion_type == "anger":
            prefix = "Z jezo odgovarjam: "
        elif self.emotion_type == "fear":
            prefix = "S strahom odgovarjam: "
        elif self.emotion_type == "joy":
            prefix = "Z veseljem odgovarjam: "

        if self.state == "Ego":
            core = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            core = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            core = "Vse resnice so eno, medsebojno povezane."

        return prefix + core
