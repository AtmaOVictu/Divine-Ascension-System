class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        shadow: "Agent | None" = None,
        angel: "Agent | None" = None,
    ) -> None:
        """Create a new agent.

        Parameters
        ----------
        name:
            Human readable identifier of the agent.
        state:
            Starting ontological phase. Must be one of :data:`STATES`.
        tension:
            Initial tension level in the ``[0, 1]`` interval. Values are
            clamped to prevent runaway growth.
        emotion:
            Initial emotional intensity in the ``[0, 1]`` interval. Values are
            also clamped.
        shadow:
            Optional reference to the agent's shadow aspect.
        angel:
            Optional reference to the agent's angelic aspect.
        """

        self.name = name
        self.state = state
        self.tension = max(0.0, min(1.0, tension))
        self.emotion = max(0.0, min(1.0, emotion))
        self.shadow = shadow
        self.angel = angel
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Set emotion and increase tension.

        The provided value is clamped to ``[0, 1]`` to avoid runaway
        amplification. Tension is increased by the same amount and clamped to
        the valid range as well.
        """
        self.emotion = max(0.0, min(1.0, value))
        self.tension = max(0.0, min(1.0, self.tension + value))

    def update_tension(self, value: float) -> None:
        """Directly set tension level with clamping."""
        self.tension = max(0.0, min(1.0, value))

    def transition(self) -> str:
        """Move to the next state if emotion or tension exceed thresholds."""
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
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
