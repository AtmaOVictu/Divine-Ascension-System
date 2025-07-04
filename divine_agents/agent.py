class Agent:
    """Ontological agent that evolves through philosophical states.

    Parameters
    ----------
    name:
        Human readable identifier of the agent.
    state:
        Starting ontological state. Defaults to "Ego".
    tension:
        Initial tension level influencing transitions.
    emotion:
        Initial emotion intensity influencing transitions.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        """Create a new agent.

        Parameters
        ----------
        name:
            Identifier for the agent.
        state:
            Initial ontological state.
        tension:
            Starting tension level.
        emotion:
            Starting emotion intensity.
        """
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Set emotion level and adjust tension.

        Parameters
        ----------
        value:
            New emotion intensity. The same value is added to ``tension``.
        """
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
        self.tension = value

    def transition(self) -> str:
        """Advance the agent to the next state when thresholds are met.

        Returns
        -------
        str
            The agent's new state after the transition.
        """
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer based on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
