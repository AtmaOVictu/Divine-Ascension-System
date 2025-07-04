class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        """Initialize an agent.

        Parameters
        ----------
        name : str
            Name of the agent.
        state : str, optional
            Initial ontological state. Must be one of :data:`STATES`.
        tension : float, optional
            Current tension level in the range 0-1.
        emotion : float, optional
            Current emotion level in the range 0-1.

        Raises
        ------
        ValueError
            If ``state`` is not a valid ontological state.
        """
        if state not in self.STATES:
            raise ValueError(f"Invalid state '{state}'. Valid states: {self.STATES}")

        self.name = name
        self.state = state
        # Clamp initial values to sensible ranges
        self.tension = max(0.0, min(1.0, tension))
        self.emotion = max(0.0, min(1.0, emotion))
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value : float
            New emotion level expected between 0 and 1. Values outside this
            range will be clamped.
        """
        self.emotion = max(0.0, min(1.0, value))
        # Increment tension with clamping
        self.tension = max(0.0, min(1.0, self.tension + self.emotion))

    def update_tension(self, value: float) -> None:
        """Directly set tension level.

        Parameters
        ----------
        value : float
            Desired tension level between 0 and 1. Values outside this range
            are clamped.
        """
        self.tension = max(0.0, min(1.0, value))

    def transition(self) -> str:
        """Perform a state transition when thresholds are exceeded.

        Transition from ``Ego`` -> ``Jaz`` or ``Jaz`` -> ``Enotnost`` when
        ``tension`` is greater than ``0.7`` or ``emotion`` greater than ``0.5``.

        Returns
        -------
        str
            The new (or unchanged) ontological state.
        """
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
