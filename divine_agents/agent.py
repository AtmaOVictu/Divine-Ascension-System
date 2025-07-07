class Agent:
    """Ontological agent capable of transitioning states and executing tasks."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        mood: str | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.mood = mood or "neutral"
        self.history: list[str] = [state]

    def update_emotion(self, mood: str, value: float) -> None:
        """Update emotion intensity and adjust tension based on mood."""
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
        """Return a philosophical answer depending on state and mood."""
        if self.state == "Ego":
            base = "Truth is absolute and independent of others."
        elif self.state == "Jaz":
            base = "Truth is relative, shaped by our relationships."
        else:
            base = "All truths are one and interconnected."

        tone = {
            "anger": " (spoken with anger)",
            "fear": " (spoken with fear)",
            "joy": " (spoken with joy)",
            "neutral": "",
        }.get(self.mood, "")

        return base + tone

    def execute_task(self, task: str, *args, **kwargs):
        """Execute an external task (ifself)."""
        from .tasks import get_weather, send_email

        if task == "get_weather":
            return get_weather(*args, **kwargs)
        if task == "send_email":
            return send_email(*args, **kwargs)
        return "Task not recognized."
