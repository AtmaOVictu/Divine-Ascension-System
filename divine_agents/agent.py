class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        The identifier of the agent.
    state:
        Starting ontological state. Defaults to ``"Ego"``.
    tension:
        Baseline tension level in the ``[0, 1]`` range.
    emotion:
        Baseline emotion intensity in the ``[0, 1]`` range.

    Agents progress through the states ``"Ego"``, ``"Jaz"`` and ``"Enotnost"``
    when their ``tension`` exceeds ``0.7`` or ``emotion`` exceeds ``0.5``.

    Example
    -------
    >>> agent = Agent("A")
    >>> agent.update_emotion(0.6)
    >>> agent.transition()
    'Jaz'
    """

    STATES = ("Ego", "Jaz", "Enotnost")

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
        value:
            New emotion intensity. The same value is added to ``tension``.
        """
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level.

        Parameters
        ----------
        value:
            New tension value.
        """
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded.

        Returns
        -------
        str
            The new state after the transition.
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
            Prompt posed to the agent. Currently unused.

        Returns
        -------
        str
            The agent's answer reflecting its view of truth.
        """
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
