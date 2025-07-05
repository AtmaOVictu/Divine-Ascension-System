from .emotion import EmotionHandler
from .philosopher import Philosopher


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        emotion_handler: EmotionHandler | None = None,
        philosopher: Philosopher | None = None,
    ) -> None:
        self.name = name
        self.emotion_handler = emotion_handler or EmotionHandler()
        self.philosopher = philosopher or Philosopher()
        self.history = [self.philosopher.state]

    @property
    def state(self) -> str:
        return self.philosopher.state

    @property
    def tension(self) -> float:
        return self.emotion_handler.tension

    @property
    def emotion(self) -> float:
        return self.emotion_handler.emotion

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion_handler.update_emotion(value)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.emotion_handler.adjust_tension(value)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.philosopher.state == "Ego":
                self.philosopher.state = "Jaz"
            elif self.philosopher.state == "Jaz":
                self.philosopher.state = "Enotnost"
        self.history.append(self.philosopher.state)
        return self.philosopher.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        return self.philosopher.respond(question)
