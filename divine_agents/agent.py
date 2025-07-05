class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        """Initialize an agent and clamp starting values between 0 and 1.

        Parameters
        ----------
        name : str
            Human readable identifier for the agent.
        state : str, optional
            Starting ontological state. Defaults to ``"Ego"``.
        tension : float, optional
            Initial tension level ``0 <= tension <= 1``.
        emotion : float, optional
            Initial emotion level ``0 <= emotion <= 1``.
        """
        self.name = name
        self.state = state
        self.tension = max(0.0, min(1.0, tension))
        self.emotion = max(0.0, min(1.0, emotion))
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly.

        The emotion value is clamped to stay between ``0`` and ``1``. The
        agent's tension is increased by the same amount and clamped as well so
        that neither attribute grows beyond the valid range.
        """
        self.emotion = max(0.0, min(1.0, value))
        self.tension = max(0.0, min(1.0, self.tension + value))

    def update_tension(self, value: float) -> None:
        """Directly set tension level, clamping it between ``0`` and ``1``."""
        self.tension = max(0.0, min(1.0, value))

    def transition(self) -> str:
        """Perform a state transition when thresholds are exceeded.

        A transition from ``Ego`` to ``Jaz`` or from ``Jaz`` to ``Enotnost``
        occurs when ``tension`` exceeds ``0.7`` or ``emotion`` exceeds ``0.5``.
        The current state is recorded in :attr:`history` after each call.

        Returns
        -------
        str
            The agent's new ontological state.
        """
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
