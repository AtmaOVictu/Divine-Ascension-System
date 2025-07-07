class Agent:
    """Represents an ontological agent capable of transitioning ontological
    states based on emotion and tension levels.

    The available states are ``Ego``, ``Jaz`` and ``Enotnost``. Transitions
    occur when either tension exceeds ``0.7`` or emotion exceeds ``0.5``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0
    ):
        """Create a new agent.

        Parameters
        ----------
        name:
            Identifier used in dialogue.
        state:
            Initial ontological state.
        tension:
            Current tension level.
        emotion:
            Current emotion intensity.
        """
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update the current emotional intensity.

        Emotion also increases tension which may trigger a state change.
        """
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
        self.tension = value

    def transition(self) -> str:
        """Transition to the next ontological state when thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the agent's state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            return f"{base} Govorim strastno."
        elif self.emotion > 0.2:
            return f"{base} Moja čustva so zaznavna."
        return base
