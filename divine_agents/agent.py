"""Core components for the ontological agent system."""


class Agent:
    """Represents an ontological agent capable of transitioning between states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    THRESHOLD_TENSION = 0.7
    THRESHOLD_EMOTION = 0.5

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value: float
            New emotion intensity. The same value is added to :attr:`tension` to
            model the coupling between emotion and tension.
        """
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition if thresholds are exceeded.

        Returns
        -------
        str
            The new state after transition (or the current state if thresholds
            are not met).
        """
        if self.tension > self.THRESHOLD_TENSION or self.emotion > self.THRESHOLD_EMOTION:
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
