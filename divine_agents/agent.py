"""Agent model representing ontological state transitions and responses."""


class Agent:
    """Ontological agent capable of emotional growth and state transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        """Create a new agent.

        Parameters
        ----------
        name:
            Human readable identifier.
        state:
            Initial ontological state. Defaults to ``"Ego"``.
        tension:
            Initial tension level.
        emotion:
            Initial emotion value.

        Side Effects
        ------------
        Initializes ``history`` with the starting state.
        """
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update the emotion level.

        Parameters
        ----------
        value:
            New emotion intensity. The same value is added to ``tension``.
        """
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Set the agent's tension level.

        Parameters
        ----------
        value:
            New tension value.
        """
        self.tension = value

    def transition(self) -> str:
        """Transition to the next state if thresholds are surpassed.

        Returns
        -------
        str
            The agent's new or current ontological state.

        Side Effects
        ------------
        Appends the resulting state to ``history``.
        """
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Respond to a question according to the current state.

        Parameters
        ----------
        question:
            A textual prompt to which the agent will respond. The content is not
            interpreted but included to mirror conversational interfaces.

        Returns
        -------
        str
            A sentence expressing the philosophical principle of the current
            state.
        """
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
