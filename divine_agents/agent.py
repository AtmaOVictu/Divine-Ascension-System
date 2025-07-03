class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition if thresholds are exceeded.

        If ``tension`` exceeds ``0.7`` or ``emotion`` exceeds ``0.5`` the agent
        moves from ``Ego`` to ``Jaz`` or from ``Jaz`` to ``Enotnost``. After a
        successful transition, both ``tension`` and ``emotion`` are reset to
        ``0.0``. Agents already in ``Enotnost`` or those with an unknown state
        remain unchanged.
        """

        # Do not transition from final or unknown states
        if self.state not in self.STATES or self.state == "Enotnost":
            self.history.append(self.state)
            return self.state

        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            # reset internal levels after a successful transition
            self.tension = 0.0
            self.emotion = 0.0

        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
