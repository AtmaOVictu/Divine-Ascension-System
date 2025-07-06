class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 emotional_state: str = "neutral", experiences=None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotional_state = emotional_state
        self.history = [state]
        self.experiences = experiences[:] if experiences else []

    def update_history(self) -> None:
        """Record the current state to the history."""
        self.history.append(self.state)

    def add_experience(self, experience: str) -> None:
        """Store an experience for later learning."""
        self.experiences.append(experience)

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        # Adjust tension based on historical experiences
        if self.state == "Ego" and "self-preservation" in self.experiences:
            self.tension = max(self.tension, 0.8)
        elif self.state == "Jaz" and "altruistic" in self.experiences:
            self.tension = max(self.tension, 0.8)

        if self.tension > 0.7 or self.emotion > 0.5:
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
