class Agent:
    """Represent an ontological agent.

    The agent holds its current ontological state, emotional intensity and
    tension. It can move from ``Ego`` to ``Jaz`` and from ``Jaz`` to
    ``Enotnost`` whenever the tension exceeds ``0.7`` or the emotion exceeds
    ``0.5``. Every state change is stored in :pyattr:`history`.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Set the emotional intensity and update tension.

        Parameters
        ----------
        value : float
            New emotional intensity in the range ``0`` to ``1``.

        The agent's tension is increased by the same amount to model the
        connection between heightened emotion and tension.
        """
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Set the tension level.

        Parameters
        ----------
        value : float
            The new tension value in the range ``0`` to ``1``.
        """
        self.tension = value

    def transition(self) -> str:
        """Attempt to transition to the next ontological state.

        The agent moves from ``Ego`` to ``Jaz`` or from ``Jaz`` to
        ``Enotnost`` when either its tension is greater than ``0.7`` or its
        emotion exceeds ``0.5``. The resulting state is appended to
        :pyattr:`history`.

        Returns
        -------
        str
            The current state after the transition check.
        """
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical statement about truth.

        Parameters
        ----------
        question : str
            Text of the question prompting the response. The value is
            currently unused.

        Returns
        -------
        str
            A reply reflecting the agent's current ontological state.
        """
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
