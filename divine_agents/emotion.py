from enum import Enum

class Emotion(Enum):
    NEUTRAL = "neutral"
    FEAR = "fear"
    JOY = "joy"
    ANGER = "anger"


class EmotionManager:
    """Manage emotional state and intensity for an agent."""

    def __init__(self, emotion: Emotion = Emotion.NEUTRAL, intensity: float = 0.0):
        self.emotion = emotion
        self.intensity = intensity

    def update(self, emotion: Emotion, intensity: float) -> None:
        self.emotion = emotion
        self.intensity = intensity

    def get_intensity(self) -> float:
        return self.intensity

