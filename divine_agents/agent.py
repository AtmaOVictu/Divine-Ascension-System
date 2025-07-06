class Agent:
    """Ontological agent capable of state transitions based on emotion and tension."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0, emotion: float = 0.0, emotion_name: str | None = None) -> None:
        """Create a new agent.

        Parameters
        ----------
        name:
            Agent identifier.
        state:
            Initial ontological state.
        tension:
            Initial tension level.
        emotion:
            Initial emotion intensity on ``0-1`` scale.
        emotion_name:
            Optional name describing the current emotion (``"fear"``, ``"joy"`` ...).
        """

        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history: list[str] = [state]

    def update_emotion(self, name: str, intensity: float) -> None:
        """Update the current emotion and adjust tension.

        Parameters
        ----------
        name:
            Descriptive emotion label.
        intensity:
            Value in ``0-1`` range representing strength of the emotion.
        """

        self.emotion_name = name
        self.emotion = intensity
        self.tension += intensity

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
        """Return a philosophical answer influenced by state and emotion."""

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.7:
            mood = "strastno"
        elif self.emotion > 0.3:
            mood = "s čustvi"
        else:
            mood = "mirno"

        return f"{mood}: {base}"
