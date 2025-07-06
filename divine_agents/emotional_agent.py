from .agent import Agent


class EmotionalAgent(Agent):
    """Agent with named emotional states influencing tension."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_state: str | None = None) -> None:
        super().__init__(name, state, tension, emotion)
        self.emotion_state = emotion_state or "brezcustven"

    def set_emotion(self, emotion_state: str, intensity: float) -> None:
        """Set emotion type and intensity, adjusting tension."""
        self.emotion_state = emotion_state
        self.update_emotion(intensity)
