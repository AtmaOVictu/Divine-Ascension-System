"""Agent module containing the core :class:`Agent` implementation."""


class Agent:
    """Ontological agent capable of state transitions and task execution."""

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

    # ------------------------------------------------------------------
    # idself methods: core identity management
    # ------------------------------------------------------------------
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
        """Perform state transition when thresholds are exceeded."""

        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer based on the current state and mood."""

        base: str
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        tone = {
            "anger": " (izrečeno z jezo)",
            "fear": " (izrečeno s strahom)",
            "joy": " (izrečeno z veseljem)",
            "neutral": "",
        }.get(self.mood, "")

        return base + tone

    # ------------------------------------------------------------------
    # ifself methods: functional behaviour
    # ------------------------------------------------------------------
    def execute_task(self, task: str, *args, **kwargs):
        """Execute a functional task such as fetching data or sending an email."""

        from . import tasks

        if task == "get_weather":
            return tasks.get_weather(*args, **kwargs)
        if task == "send_email":
            return tasks.send_email(*args, **kwargs)
        return "Task not recognized."

