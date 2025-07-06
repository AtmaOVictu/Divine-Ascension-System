class Agent:
    """Ontological agent that can transition between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    PHILOSOPHY = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_type: str | None = None,
    ) -> None:
        """Create a new agent.

        Parameters
        ----------
        name:
            Identifier of the agent.
        state:
            Initial ontological state.
        tension:
            Accumulated tension. If it exceeds ``0.7`` the agent may change
            state.
        emotion:
            Emotional intensity. If it exceeds ``0.5`` the agent may also change
            state.
        emotion_type:
            Current emotion label (e.g. ``fear`` or ``joy``). It is optional and
            used only to enrich dialogue output.
        """
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history: list[str] = [state]

    def __repr__(self) -> str:
        return (
            f"Agent(name={self.name!r}, state={self.state!r}, "
            f"tension={self.tension:.2f}, emotion={self.emotion:.2f}, "
            f"emotion_type={self.emotion_type!r})"
        )

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and, optionally, the emotion label.

        The new emotion value also increases the agent's tension, modelling how
        strong feelings raise inner pressure.
        """
        self.emotion = value
        if emotion_type is not None:
            self.emotion_type = emotion_type
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition if emotional thresholds are met."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state."""
        base = self.PHILOSOPHY.get(self.state, "")
        if self.emotion_type:
            return f"[{self.emotion_type}] {base}"
        return base
