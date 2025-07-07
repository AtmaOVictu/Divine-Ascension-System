class Agent:
    """Represents an ontological agent capable of transitioning between
    philosophical states based on emotion and tension."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, mood: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.mood = mood or "neutral"
        self.history: list[str] = [state]

    def update_emotion(self, mood: str, value: float) -> None:
        """Update emotion intensity and adjust tension based on emotion type."""
        self.mood = mood
        self.emotion = value
        if mood in ("fear", "anger"):
            self.tension += value
        elif mood == "joy":
            self.tension -= value
        else:
            self.tension += value / 2

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition when tension or emotion passes thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state and mood."""
        base: str
        if self.state == "Ego":
            base = "Truth is absolute and independent of others."
        elif self.state == "Jaz":
            base = "Truth is relative, shaped by our relationships."
        else:
            base = "All truths are one and interconnected."

        if self.mood == "anger":
            tone = " (spoken with anger)"
        elif self.mood == "fear":
            tone = " (spoken with fear)"
        elif self.mood == "joy":
            tone = " (spoken with joy)"
        else:
            tone = ""

        return base + tone
