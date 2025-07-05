class Agent:
    """Ontological agent capable of evolving through philosophical states.

    Parameters
    ----------
    name : str
        The agent's identifier.
    state : str, optional
        Starting ontological state. Must be one of :pyattr:`STATES`.
    tension : float, optional
        Initial tension level. Values are clamped between ``0`` and ``1``.
    emotion : float, optional
        Initial emotion intensity. Values are clamped between ``0`` and ``1``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        # Clamp starting values to avoid runaway growth
        self.name = name
        self.state = state if state in self.STATES else "Ego"
        self.tension = max(0.0, min(1.0, tension))
        self.emotion = max(0.0, min(1.0, emotion))
        self.history = [self.state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and increase tension.

        Parameters
        ----------
        value : float
            New emotion level. The value is clamped between ``0`` and ``1``.

        Notes
        -----
        The agent's tension is increased by the final emotion value. Both
        emotion and tension are kept within the ``0``-``1`` range.
        """

        self.emotion = max(0.0, min(1.0, value))
        self.tension = max(0.0, min(1.0, self.tension + self.emotion))

    def update_tension(self, value: float) -> None:
        """Set the agent's tension level.

        Parameters
        ----------
        value : float
            Desired tension level which will be clamped between ``0`` and ``1``.
        """

        self.tension = max(0.0, min(1.0, value))

    def transition(self) -> str:
        """Transition to the next ontological state when limits are met.

        The agent moves from ``Ego`` to ``Jaz`` or from ``Jaz`` to ``Enotnost``
        whenever tension exceeds ``0.7`` or emotion exceeds ``0.5``. The state
        remains unchanged otherwise. Each transition is recorded in
        :pyattr:`history`.
        """

        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Answer a philosophical question based on the agent's state."""

        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
