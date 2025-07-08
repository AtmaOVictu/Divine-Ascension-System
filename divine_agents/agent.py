class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        """Create a new agent.

        Parameters
        ----------
        name : str
            Identifier used in dialogue.
        state : str, optional
            Ontological state of the agent, by default ``"Ego"``.
        tension : float, optional
            Current tension level, by default ``0.0``.
        emotion : float, optional
            Current emotion intensity, by default ``0.0``.
        """
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        # Keep track of all states the agent has occupied.
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Set emotion intensity and increase tension.

        The provided value represents how strongly the agent feels a
        particular emotion. Increasing emotional intensity also raises
        ``tension`` to reflect the mounting internal pressure that may
        provoke a state change.
        """
        self.emotion = value
        # Heightened emotion contributes directly to overall tension.
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly assign a new tension level."""
        self.tension = value

    def transition(self) -> str:
        """Move to the next state if emotion or tension crosses a threshold.

        Returns
        -------
        str
            The agent's new state after evaluation.
        """
        # State changes occur only when the agent is sufficiently
        # emotional or tense. Thresholds are defined by the system's rules.
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Provide a philosophical reply reflecting the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
