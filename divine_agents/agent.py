class Agent:
    """Represent an ontological agent capable of state transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotions: dict | None = None) -> None:
        """Initialize the agent with a name, state and optional emotions.

        Parameters
        ----------
        name:
            Agent identifier.
        state:
            Starting ontological state.
        tension:
            Initial tension level.
        emotions:
            Mapping of emotion names (e.g. ``"fear"``) to intensity ``0-1``.
        """

        self.name = name
        self.state = state
        self.tension = tension
        self.emotions: dict[str, float] = emotions or {"fear": 0.0, "joy": 0.0, "anger": 0.0}
        self.history = [state]

    def update_emotion(self, name: str, value: float) -> None:
        """Update a specific emotion and adjust tension.

        Parameters
        ----------
        name:
            Name of the emotion to modify.
        value:
            Intensity of the emotion ``0-1``. Values outside this range are
            clamped.
        """

        value = max(0.0, min(1.0, value))
        self.emotions[name] = value
        self.tension += value

    def emotion_intensity(self) -> float:
        """Return the highest emotion intensity."""
        return max(self.emotions.values(), default=0.0)

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_intensity() > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        prefix = ""
        emotion, level = max(self.emotions.items(), key=lambda item: item[1])
        if level > 0.5:
            prefix = f"Občutim {emotion}, vendar "

        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."
