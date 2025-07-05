class Agent:
    """Represents an ontological agent capable of transitioning states.

    An agent maintains a current ontological state and records every change in
    ``history``. State transitions occur when either the ``tension`` or
    ``emotion`` attributes exceed their respective thresholds.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        """Create a new agent.

        Parameters
        ----------
        name:
            Identifier of the agent.
        state:
            Initial ontological state. Defaults to ``"Ego"``.
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
        """Update emotion intensity and adjust tension accordingly.

        Emotion directly influences the agent's tension. A sufficiently high
        emotion can therefore trigger a state change when :py:meth:`transition`
        is called.

        Parameters
        ----------
        value:
            New emotion value in the range ``0.0`` to ``1.0``.
        """
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level.

        Parameters
        ----------
        value:
            New tension value in the range ``0.0`` to ``1.0``.
        """
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded.

        The agent progresses from ``Ego`` → ``Jaz`` or ``Jaz`` → ``Enotnost``
        if ``tension`` exceeds ``0.7`` or ``emotion`` exceeds ``0.5``. Each
        invocation appends the resulting state to ``history``.

        Returns
        -------
        str
            The state the agent occupies after attempting the transition.
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
            The question posed to the agent. Currently unused but included for
            future extension.

        Returns
        -------
        str
            A textual answer reflecting the agent's ontological view of truth.
        """
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
