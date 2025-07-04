class Agent:
    """Ontological agent capable of state transitions.

    The agent moves between the philosophical states ``Ego``, ``Jaz`` and
    ``Enotnost`` based on its current ``tension`` and ``emotion`` levels.
    ``tension`` grows when emotions rise and once thresholds are passed the
    agent transitions to the next state.

    Attributes
    ----------
    name: str
        Human friendly name of the agent.
    state: str
        Current ontological state.
    tension: float
        Amount of tension accumulated in the agent.
    emotion: float
        Current emotion intensity.
    history: List[str]
        States the agent has visited in chronological order.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        """Create a new agent instance.

        Parameters
        ----------
        name : str
            The agent's display name.
        state : str, optional
            Starting ontological state. Defaults to ``"Ego"``.
        tension : float, optional
            Initial tension value. Defaults to ``0.0``.
        emotion : float, optional
            Initial emotion intensity. Defaults to ``0.0``.
        """

        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value : float
            New emotion value. This value is also added to ``tension``.

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
            New tension level for the agent.

        Returns
        -------
        None
        """
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded.

        The agent moves from ``Ego`` to ``Jaz`` or from ``Jaz`` to
        ``Enotnost`` when either ``tension`` is greater than ``0.7`` or
        ``emotion`` is greater than ``0.5``. The resulting state is stored in
        ``history``.

        Returns
        -------
        str
            The new or unchanged state after evaluating the thresholds.
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
        question : str
            Text of the question being asked. Currently unused but allows
            future expansion.

        Returns
        -------
        str
            Response string reflecting the agent's ontological perspective.
        """
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
