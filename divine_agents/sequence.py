from .agent import Agent


class LogicalSequenceAgent(Agent):
    """Agent with automated logical state transitions."""

    def __init__(self, name: str, state: str = "Ego", *, tension_threshold: float = 0.7,
                 emotion_threshold: float = 0.5):
        super().__init__(name, state)
        self.tension_threshold = tension_threshold
        self.emotion_threshold = emotion_threshold

    def evaluate_condition(self, tension: float, emotion: float) -> None:
        """Update emotion/tension and transition if thresholds are met."""
        self.update_tension(tension)
        self.update_emotion(emotion)
        if self.state == "Ego" and (
            self.tension > self.tension_threshold or self.emotion > self.emotion_threshold
        ):
            self.state = "Jaz"
        elif self.state == "Jaz" and (
            self.tension > self.tension_threshold or self.emotion > self.emotion_threshold
        ):
            self.state = "Enotnost"
        self.history.append(self.state)

    def perform_action(self) -> str:
        """Return the philosophical response of the current state."""
        return self.respond("Kaj je resnica?")

    def execute_sequence(self, tension: float, emotion: float) -> str:
        """Execute a full evaluation and action step."""
        self.evaluate_condition(tension, emotion)
        return self.perform_action()
