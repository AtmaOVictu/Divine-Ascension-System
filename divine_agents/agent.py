class Agent:
    """Ontological agent capable of emotional state transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_level = 0.0
        self.emotion_type = "neutral"
        self.history = [state]

    def update_emotion(self, level: float, emotion_type: str = "neutral") -> None:
        """Update emotion intensity and type, adjusting tension."""
        self.emotion_level = level
        self.emotion_type = emotion_type
        self.tension += level

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def _should_transition(self) -> bool:
        """Determine if thresholds for transition are met."""
        return self.tension > 0.7 or self.emotion_level > 0.5

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self._should_transition():
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer based on state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        prefix = ""
        if self.emotion_type == "fear":
            prefix = "S trepetom povem: "
        elif self.emotion_type == "anger":
            prefix = "Z jezo zatrdim: "
        elif self.emotion_type == "joy":
            prefix = "Z veseljem razlagam: "

        return f"{prefix}{base}"
