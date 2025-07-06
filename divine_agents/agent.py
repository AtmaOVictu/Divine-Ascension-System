class Agent:
    """Ontological agent that can shift states based on emotion and tension."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str) -> None:
        """Update emotion intensity and adjust tension based on type."""
        self.emotion = value
        self.emotion_type = emotion_type
        if emotion_type in {"fear", "anger"}:
            self.tension = min(1.0, self.tension + value)
        elif emotion_type == "joy":
            self.tension = max(0.0, self.tension - value / 2)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Shift ontological state when thresholds are reached."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a state-dependent answer influenced by emotion."""
        prefix = {
            "fear": "S strahom verjamem,",
            "joy": "Z veseljem verjamem,",
            "anger": "Z jezo izjavljam,",
        }.get(self.emotion_type, "Mirno povem,")

        if self.state == "Ego":
            core = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            core = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            core = "Vse resnice so eno, medsebojno povezane."

        return f"{prefix} {core}"
