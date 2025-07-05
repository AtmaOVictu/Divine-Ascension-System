class Agent:
    """Represents an ontological agent capable of transitioning states.

    Each agent carries a ``shadow`` value representing its inherent
    contradiction. Emotion and shadow together influence the agent's
    tension, which in turn drives ontological state transitions.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, shadow: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.shadow = shadow
        self.history = [state]

    def update_emotion(self, value: float, shadow: float | None = None) -> None:
        """Update emotion intensity and optionally update the shadow.

        The agent's tension increases with the sum of emotion and shadow,
        reflecting the inherent contradiction between feelings and their
        opposite.
        """
        self.emotion = value
        if shadow is not None:
            self.shadow = shadow
        self.tension += value + self.shadow

    def update_shadow(self, value: float) -> None:
        """Set the agent's shadow and adjust tension accordingly."""
        self.shadow = value
        self.tension += value

    def get_state(self) -> tuple[float, float, float]:
        """Return current tension, emotion and shadow."""
        return self.tension, self.emotion, self.shadow

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state and emotion."""
        prefix = "" if self.emotion <= 0.5 else "(čustveno) "
        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."
