class Agent:
    """Represent an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type or "neutral"
        self.history: list[str] = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and adjust tension based on emotion type."""
        self.emotion = value
        if emotion_type:
            self.emotion_type = emotion_type
        # Fear and anger produce stronger tension than joy or neutral emotions
        modifier = 1.0 if self.emotion_type in {"fear", "anger"} else 0.5
        self.tension = min(1.0, self.tension + value * modifier)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, min(1.0, value))

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
        """Return a philosophical answer that reflects state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_type == "fear":
            mood = "S strahom"
        elif self.emotion_type == "anger":
            mood = "Z jezo"
        elif self.emotion_type == "joy":
            mood = "Z veseljem"
        else:
            mood = ""

        statement = f"{mood} {base}".strip()
        return statement
