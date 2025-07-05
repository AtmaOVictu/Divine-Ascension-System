from __future__ import annotations

from typing import Tuple

from .agent import Agent


class LogicalSequenceAgent(Agent):
    """Agent that automates transitions based on logical sequences."""

    def __init__(self, name: str, state: str = "Ego", *,
                 tension_threshold: float = 0.7, emotion_threshold: float = 0.5,
                 tension: float = 0.0, emotion: float = 0.0) -> None:
        super().__init__(name, state=state, tension=tension, emotion=emotion)
        self.tension_threshold = tension_threshold
        self.emotion_threshold = emotion_threshold

    def evaluate_condition(self, tension: float, emotion: float) -> None:
        """Update internal values and trigger a state transition if needed."""
        self.update_tension(tension)
        self.update_emotion(emotion)
        if self.tension > self.tension_threshold or self.emotion > self.emotion_threshold:
            self.transition()

    def perform_action(self) -> str:
        """Return the agent's philosophical response."""
        return self.respond("Kaj je resnica?")

    def execute_sequence(self, tension: float, emotion: float) -> Tuple[str, str, str]:
        """Automate update, transition and response generation.

        Returns a tuple of (previous_state, new_state, reply).
        """
        prev_state = self.state
        self.evaluate_condition(tension, emotion)
        reply = self.perform_action()
        return prev_state, self.state, reply
