class Agent:
    """Ontological agent capable of transitioning states and executing tasks."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, mood: str | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.mood = mood or "neutral"
        self.history = [state]

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
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on state and current mood."""
        base: str
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        tone = {
            "anger": " (izgovorjeno z jezo)",
            "fear": " (izgovorjeno s strahom)",
            "joy": " (izgovorjeno z veseljem)",
            "neutral": "",
        }.get(self.mood, "")

        return base + tone

    def execute_task(self, task: str, *args, **kwargs):
        """Handle functional tasks such as external calls."""
        if task == "get_weather":
            return get_weather(*args, **kwargs)
        if task == "send_email":
            return send_email(*args, **kwargs)
        return "Task not recognized."


def get_weather(location: str) -> str:
    """Return mock weather information for the provided location."""
    return f"Vreme v {location} je sončno."  # simple placeholder


def send_email(to: str, body: str) -> str:
    """Simulate sending an email."""
    return f"Email poslano prejemniku {to} z vsebino: {body}"
