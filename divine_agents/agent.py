class Agent:
    """Represent an ontological agent with emotional dynamics."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, mood: str | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.mood = mood or "neutral"
        self.history = [state]

    def update_emotion(self, value: float, mood: str | None = None) -> None:
        """Update emotion intensity and adjust tension according to mood."""
        self.emotion = value
        if mood:
            self.mood = mood
        if self.mood in {"fear", "anger"}:
            self.tension += value
        else:
            self.tension += value / 2

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
        """Return a philosophical answer depending on the current state."""
        prefix = ""
        if self.mood == "fear":
            prefix = "S strahom, "
        elif self.mood == "anger":
            prefix = "Z jezo, "
        elif self.mood == "joy":
            prefix = "Z veseljem, "

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{prefix}{base}"
