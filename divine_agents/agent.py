class Agent:
    """Ontological agent capable of state transitions based on emotion and tension."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_label: str | None = None,
    ) -> None:
        """Create a new agent with an initial ontological state.

        Parameters
        ----------
        name:
            Identifier for the agent.
        state:
            Starting ontological state, defaults to ``"Ego"``.
        tension:
            Initial tension level.
        emotion:
            Initial emotion intensity.
        emotion_label:
            Optional label describing the current emotion (e.g. ``"fear"``).
        """

        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history: list[str] = [state]

    def update_emotion(self, value: float, label: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            New emotion intensity between ``0`` and ``1``.
        label:
            Optional description of the emotion (e.g. ``"joy"``).
        """

        self.emotion = value
        self.tension += value
        if label is not None:
            self.emotion_label = label

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""

        self.tension = value

    def transition(self) -> str:
        """Perform a state transition when emotion or tension exceed thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return an answer reflecting the agent's state and emotion."""

        prefix = f"({self.emotion_label}) " if self.emotion_label else ""

        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."
