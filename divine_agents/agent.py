class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        """Initialize the agent.

        Parameters
        ----------
        name:
            Agent identifier.
        state:
            Initial ontological state.
        tension:
            Initial tension value.
        emotion:
            Initial emotion intensity.
        emotion_type:
            Type of current emotion (e.g. ``fear``, ``joy``).
        """

        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        if emotion_type is not None:
            self.emotion_type = emotion_type
        self.tension += value

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

    def _emotion_prefix(self) -> str:
        """Return a short phrase based on the current emotion."""
        mapping = {
            "fear": "V strahu",
            "joy": "Z veseljem",
            "anger": "Z jezo",
        }
        return mapping.get(self.emotion_type, "")

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        prefix = self._emotion_prefix()
        if self.state == "Ego":
            core = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            core = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            core = "Vse resnice so eno, medsebojno povezane."
        return f"{prefix} {core}".strip()
