"""Core classes for modelling agents and their ontological transitions."""


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        """Create a new agent.

        Args:
            name: Agent's identifier.
            state: Initial ontological state.
            tension: Initial tension level between 0 and 1.
            emotion: Initial emotion intensity between 0 and 1.

        Returns:
            None
        """
        self.name = name
        self.state = state
        self.tension = max(0.0, min(tension, 1.0))
        self.emotion = max(0.0, min(emotion, 1.0))
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Args:
            value: New emotion level between 0 and 1.

        Returns:
            None
        """
        self.emotion = max(0.0, min(value, 1.0))
        self.tension = min(1.0, self.tension + self.emotion)

    def update_tension(self, value: float) -> None:
        """Directly set tension level.

        Args:
            value: New tension level between 0 and 1.

        Returns:
            None
        """
        self.tension = max(0.0, min(value, 1.0))

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded.

        The agent moves from ``Ego`` to ``Jaz`` or from ``Jaz`` to ``Enotnost``
        when either the tension exceeds ``0.7`` or the emotion exceeds ``0.5``.
        After a successful transition the current emotion level is reset.

        Returns:
            str: The ontological state after the transition attempt.
        """
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            self.emotion = 0.0
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state.

        Args:
            question: Ignored textual question from another agent.

        Returns:
            str: An answer reflecting the agent's ontological perspective.
        """
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
