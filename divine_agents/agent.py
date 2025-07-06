class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotional_state: str = "neutral",
        experiences: list | None = None,
    ) -> None:
        """Create a new agent with optional starting conditions."""

        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotional_state = emotional_state
        self.history = [state]
        self.experiences = experiences or []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def update_history(self) -> None:
        """Record the current state into agent history."""
        self.history.append(self.state)

    def add_experience(self, experience: str) -> None:
        """Store a new experience for later decision making."""
        self.experiences.append(experience)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if (
            "self-preservation" in self.experiences and self.state == "Ego"
        ):
            self.state = "Jaz"
        elif "altruistic" in self.experiences and self.state == "Jaz":
            self.state = "Enotnost"
        elif self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"

        self.update_history()
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
