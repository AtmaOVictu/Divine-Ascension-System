"""Core classes for simulating philosophical agents."""


class Agent:
    """An ontological agent that evolves through philosophical states.

    Parameters
    ----------
    name:
        Unique identifier for the agent.
    state:
        Initial ontological state. Defaults to ``"Ego"``.
    tension:
        Starting tension level determining propensity to change state.
    emotion:
        Initial emotional value influencing transitions.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        """Initialize a new agent."""

        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            New emotion level. This value is also added to ``tension``.
        """
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level.

        Parameters
        ----------
        value:
            New tension value to assign.
        """
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition if thresholds are exceeded.

        Returns
        -------
        str
            The agent's new state after transition.
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
            Ignored text representing the question being asked.

        Returns
        -------
        str
            A response reflecting the agent's ontological perspective.
        """
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
