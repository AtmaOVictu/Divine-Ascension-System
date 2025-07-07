class Agent:
    """Ontological agent capable of state transitions based on emotion and tension."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_type: str | None = None,
    ):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type or ""
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str) -> None:
        """Update emotion intensity and adjust tension based on emotion type."""
        self.emotion = value
        self.emotion_type = emotion_type

        if emotion_type in {"fear", "anger"}:
            self.tension += value
        elif emotion_type == "joy":
            self.tension = max(0.0, self.tension - value / 2)
        else:
            self.tension += value / 2

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition if emotion or tension exceed thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by current state and emotion."""
        prefix = ""
        if self.emotion_type == "fear":
            prefix = "V strahu odgovarjam: "
        elif self.emotion_type == "anger":
            prefix = "Z jezo odgovarjam: "
        elif self.emotion_type == "joy":
            prefix = "Z veseljem odgovarjam: "

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{prefix}{base}"
