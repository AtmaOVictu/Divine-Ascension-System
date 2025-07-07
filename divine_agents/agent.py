class Agent:
    """Ontological agent capable of emotional state transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: dict | None = None):
        """Initialize the agent with optional emotion information.

        Parameters
        ----------
        name:
            Identifier for the agent.
        state:
            Initial ontological state.
        tension:
            Starting tension level.
        emotion:
            Optional dict describing current emotion ``{"type": str, "intensity": float}``.
        """

        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion or {"type": "neutral", "intensity": 0.0}
        self.history = [state]

    def set_emotion(self, kind: str, intensity: float) -> None:
        """Set the current emotion and adjust tension accordingly."""
        self.emotion = {"type": kind, "intensity": intensity}
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion.get("intensity", 0.0) > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        base: str
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        emotion_note = f" Čutim {self.emotion['type']}." if self.emotion['type'] != 'neutral' else ""
        return base + emotion_note
