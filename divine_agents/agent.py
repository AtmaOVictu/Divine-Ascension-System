class Agent:
    """Represent an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Identifier for the agent.
    state:
        Starting ontological state. One of ``Ego``, ``Jaz`` or ``Enotnost``.
    tension:
        Initial tension level ranging from 0 to 1.
    emotion:
        Initial emotion intensity ranging from 0 to 1.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        # Clamp starting values to keep them within valid bounds
        self.tension = max(0.0, min(1.0, tension))
        self.emotion = max(0.0, min(1.0, emotion))
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly.

        The resulting values are clamped between 0 and 1 to prevent
        runaway growth.
        """
        self.emotion = max(0.0, min(1.0, value))
        self.tension = max(0.0, min(1.0, self.tension + self.emotion))

    def update_tension(self, value: float) -> None:
        """Directly set tension level, clamped between 0 and 1."""
        self.tension = max(0.0, min(1.0, value))

    def transition(self) -> str:
        """Transition the agent to a new state if thresholds are exceeded.

        The agent moves from ``Ego`` -> ``Jaz`` or ``Jaz`` -> ``Enotnost``
        when ``tension`` exceeds 0.7 or ``emotion`` exceeds 0.5. No
        transition occurs beyond ``Enotnost``.
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
