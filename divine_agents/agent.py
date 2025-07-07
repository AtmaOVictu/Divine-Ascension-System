class Agent:
    """Ontological agent that can transition between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
    ) -> None:
        """Initialize the agent and its emotional context.

        Parameters
        ----------
        name : str
            Agent identifier.
        state : str, optional
            Initial ontological state. Defaults to ``"Ego"``.
        tension : float, optional
            Starting tension level. Defaults to ``0.0``.
        emotion : float, optional
            Starting emotion intensity. Defaults to ``0.0``.

        Returns
        -------
        None
        """
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Set emotion intensity and adjust tension.

        Parameters
        ----------
        value : float
            New emotion value.

        Returns
        -------
        None
        """
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level.

        Parameters
        ----------
        value : float
            New tension level.

        Returns
        -------
        None
        """
        self.tension = value

    def transition(self) -> str:
        """Transition to the next state if thresholds are exceeded.

        Returns
        -------
        str
            The new or current state after evaluation.
        """
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer based on the current state.

        Parameters
        ----------
        question : str
            Prompt being answered. The value is ignored but included for
            interface compatibility.

        Returns
        -------
        str
            Textual answer that reflects the agent's ontological state.
        """
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
