class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        """Initialize the agent with its starting values.

        Parameters
        ----------
        name : str
            Display name of the agent.
        state : str, optional
            Initial ontological state, by default ``"Ego"``.
        tension : float, optional
            Starting tension level which may trigger transitions, by default ``0.0``.
        emotion : float, optional
            Starting emotion intensity, by default ``0.0``.
        """

        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Set a new emotion level and adjust tension.

        Parameters
        ----------
        value : float
            The new emotion intensity which also increases ``tension``.
        """

        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly assign the agent's tension level.

        Parameters
        ----------
        value : float
            New tension value to be stored.
        """

        self.tension = value

    def transition(self) -> str:
        """Trigger a state change if emotion or tension exceed thresholds.

        Returns
        -------
        str
            The new ontological state after evaluating thresholds.
        """

        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Provide a philosophical answer based on the agent's state.

        Parameters
        ----------
        question : str
            The prompt being answered (currently unused).

        Returns
        -------
        str
            A textual reply corresponding to the current ontological state.
        """

        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
