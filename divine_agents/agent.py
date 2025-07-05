class Agent:
    """Represents an ontological agent capable of transitioning between states.

    Parameters
    ----------
    name : str
        Human readable agent identifier.
    state : str, optional
        Starting ontological state, defaults to ``"Ego"``.
    tension : float, optional
        Initial tension level in the range ``0`` to ``1``.
    emotion : float, optional
        Initial emotion intensity in the range ``0`` to ``1``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = max(0.0, min(1.0, tension))
        self.emotion = max(0.0, min(1.0, emotion))
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value : float
            Emotion delta to apply. The resulting emotion is clamped
            to the ``0``--``1`` range.
        """
        self.emotion = max(0.0, min(1.0, self.emotion + value))
        self.tension = max(0.0, min(1.0, self.tension + value))

    def update_tension(self, value: float) -> None:
        """Directly set tension level.

        Parameters
        ----------
        value : float
            Absolute tension value which will be clamped to ``0``--``1``.
        """
        self.tension = max(0.0, min(1.0, value))

    def transition(self) -> str:
        """Transition to the next ontological state when thresholds are exceeded.

        Returns
        -------
        str
            The agent's new state.
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
            Input question (unused but kept for extensibility).

        Returns
        -------
        str
            Philosophical statement reflecting the agent's state.
        """
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
