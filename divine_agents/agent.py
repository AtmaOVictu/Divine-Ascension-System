class Agent:
    """Represent an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str | None = None) -> None:
        """Initialize the agent.

        Parameters
        ----------
        name:
            Identifier for the agent.
        state:
            Initial ontological state.
        tension:
            Initial tension level.
        emotion:
            Initial emotion intensity.
        emotion_type:
            Descriptive label of the current emotion (e.g. ``"fear"``).
        """

        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type or "neutral"
        self.history: list[str] = [state]

    def update_emotion(self, value: float, label: str | None = None) -> None:
        """Update emotion intensity and optionally its descriptive label."""
        self.emotion = value
        if label:
            self.emotion_type = label
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

    def respond(self, question: str) -> str:
        """Return a philosophical answer reflecting the current state and emotion."""
        if self.state == "Ego":
            return (
                f"Kot {self.emotion_type} posameznik menim, da je resnica absolutna "
                "in neodvisna od drugih."
            )
        if self.state == "Jaz":
            return (
                f"Ob {self.emotion_type} obcutkih dojemam resnico kot relativno, "
                "oblikovano z nasimi odnosi."
            )
        return (
            f"Z {self.emotion_type} v srcu verjamem, da so vse resnice eno, "
            "medsebojno povezane."
        )
