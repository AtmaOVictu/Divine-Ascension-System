from __future__ import annotations

from .emotion import EmotionHandler
from .philosopher import Philosopher


class Agent:
    """Ontological agent capable of transitioning philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        *,
        emotion_handler: EmotionHandler | None = None,
        philosopher: Philosopher | None = None,
    ) -> None:
        self.name = name
        self.emotion_handler = emotion_handler or EmotionHandler(
            initial_emotion=emotion, initial_tension=tension
        )
        self.philosopher = philosopher or Philosopher(state=state)
        self.history = [self.philosopher.state]

    # Convenience properties -------------------------------------------------
    @property
    def state(self) -> str:  # pragma: no cover - simple delegation
        return self.philosopher.state

    @property
    def tension(self) -> float:  # pragma: no cover - simple delegation
        return self.emotion_handler.tension

    @property
    def emotion(self) -> float:  # pragma: no cover - simple delegation
        return self.emotion_handler.emotion

    # API methods ------------------------------------------------------------
    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension."""
        self.emotion_handler.update_emotion(value)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.emotion_handler.adjust_tension(value)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if (
            self.emotion_handler.tension > 0.7
            or self.emotion_handler.emotion > 0.5
        ):
            if self.philosopher.state == "Ego":
                self.philosopher.state = "Jaz"
            elif self.philosopher.state == "Jaz":
                self.philosopher.state = "Enotnost"
        self.history.append(self.philosopher.state)
        return self.philosopher.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer based on the current state."""
        return self.philosopher.respond(question)
