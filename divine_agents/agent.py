class Agent:
    """Represent an ontological agent that can evolve through philosophical
    states based on its emotions and tension level.

    The agent starts in ``Ego`` and may progress to ``Jaz`` or ``Enotnost``
    when the corresponding thresholds are exceeded.  Each call that updates
    emotion or tension stores the new state in ``history`` after a potential
    transition.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Set the current emotional intensity and adjust tension.

        Parameters
        ----------
        value:
            New absolute emotional value in the ``[0, 1]`` interval.
        """
        self.emotion = value
        self.tension = max(0.0, min(1.0, self.tension + value))

    def update_tension(self, value: float) -> None:
        """Directly set the tension level in ``[0, 1]``."""
        self.tension = max(0.0, min(1.0, value))

    def feel(self, delta: float) -> None:
        """Increment emotion and tension by ``delta``.

        This method simulates an emotional reaction.  Both emotion and
        tension increase by ``delta`` and are clamped to ``[0, 1]``.
        """
        self.update_emotion(max(0.0, min(1.0, self.emotion + delta)))

    def transition(self) -> str:
        """Perform a state transition if thresholds are exceeded.

        The agent moves from ``Ego`` to ``Jaz`` or from ``Jaz`` to
        ``Enotnost`` when either tension is above ``0.7`` or emotion is above
        ``0.5``.  The state remains unchanged otherwise.  Every call appends
        the resulting state to ``history``.
        """
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer that reflects the current state.

        The tone of the answer subtly changes with the current emotional
        intensity.  Higher emotion results in a more emphatic statement.
        """
        emphasis = "!" if self.emotion > 0.5 else "."
        if self.state == "Ego":
            return f"Resnica je absolutna in neodvisna od drugih{emphasis}"
        if self.state == "Jaz":
            return f"Resnica je relativna, oblikovana z našimi odnosi{emphasis}"
        return f"Vse resnice so eno, medsebojno povezane{emphasis}"
