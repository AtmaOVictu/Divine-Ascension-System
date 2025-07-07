class Agent:
    """Ontological agent capable of transitioning between states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, emotion: str, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion_type = emotion
        self.emotion = value
        if emotion in {"fear", "anger"}:
            self.tension += value
        elif emotion == "joy":
            self.tension -= value / 2
        else:
            self.tension += value / 4
        self.tension = max(0.0, min(1.0, self.tension))

    def update_tension(self, value: float) -> None:
        """Directly set tension level within [0, 1]."""
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
        """Return a philosophical answer depending on the current state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_type == "fear":
            return base + " (govori prestrašeno)"
        if self.emotion_type == "anger":
            return base + " (govori jezno)"
        if self.emotion_type == "joy":
            return base + " (govori radostno)"
        return base
