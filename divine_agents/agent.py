class Agent:
    """Ontological agent capable of state transitions and emotional expression."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *,
                 tension: float = 0.0, emotion: float = 0.0,
                 emotion_label: str | None = None, express_emotion: bool = True) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.express_emotion = express_emotion
        self.history = [state]

    # ------------------------------------------------------------------
    # Emotional handling
    # ------------------------------------------------------------------
    def set_emotion(self, label: str, value: float) -> None:
        """Set emotion label and intensity, adjusting tension accordingly."""
        self.emotion_label = label
        self.emotion = value
        self.tension += value

    def hide_emotion(self, hide: bool = True) -> None:
        """Toggle visibility of emotional expression."""
        self.express_emotion = not hide

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    # ------------------------------------------------------------------
    # State logic
    # ------------------------------------------------------------------
    def transition(self) -> str:
        """Perform a state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    # ------------------------------------------------------------------
    # Response logic
    # ------------------------------------------------------------------
    def respond(self, question: str) -> str:
        """Return a philosophical answer reflecting state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.express_emotion and self.emotion_label:
            return f"{base} ({self.emotion_label})"
        return base
