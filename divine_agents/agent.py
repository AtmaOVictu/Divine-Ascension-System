class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension.

        Parameters
        ----------
        value: float
            Desired emotion intensity. Values outside ``[0.0, 1.0]`` are
            clamped. The agent's tension is increased by the same normalized
            amount but will never exceed ``1.0``.
        """

        normalized = max(0.0, min(1.0, value))
        self.emotion = normalized
        self.tension = min(1.0, self.tension + normalized)

    def update_tension(self, value: float) -> None:
        """Directly set tension level.

        Any value outside ``[0.0, 1.0]`` is clamped to ensure tension remains
        within valid bounds.
        """
        self.tension = max(0.0, min(1.0, value))

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
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
