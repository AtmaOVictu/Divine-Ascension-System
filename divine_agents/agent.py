class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        """Initialize a new agent.

        Parameters
        ----------
        name:
            Name of the agent.
        state:
            Starting ontological state. Defaults to ``"Ego"``.
        tension:
            Initial tension level between 0 and 1.
        emotion:
            Initial emotion intensity between 0 and 1.
        """
        self.name = name
        self.state = state
        # Clamp incoming values to avoid unbounded growth
        self.tension = max(0.0, min(tension, 1.0))
        self.emotion = max(0.0, min(emotion, 1.0))
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            New emotion intensity.
        """
        self.emotion = max(0.0, min(value, 1.0))
        self.tension = max(0.0, min(self.tension + value, 1.0))

    def update_tension(self, value: float) -> None:
        """Directly set tension level.

        Parameters
        ----------
        value:
            Tension intensity to set.
        """
        self.tension = max(0.0, min(value, 1.0))

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded.

        Returns
        -------
        str
            The new ontological state after transition.
        """
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state.

        Parameters
        ----------
        question:
            The question posed to the agent.

        Returns
        -------
        str
            The agent's philosophical response.
        """
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
