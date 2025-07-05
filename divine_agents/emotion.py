import math

class EmotionTransformer:
    """Transform emotion values between negative and positive spectrums."""

    def __init__(self, emotion_value: float, k: float = 1.0) -> None:
        self.emotion_value = max(min(emotion_value, 1.0), -1.0)
        self.k = k

    def transform_positive(self) -> float:
        """Map negative emotion toward the positive range using a sigmoid."""
        if self.emotion_value < 0:
            return 1 / (1 + math.exp(-self.k * self.emotion_value))
        return self.emotion_value

    def transform_negative(self) -> float:
        """Map positive emotion toward the negative range using a sigmoid."""
        if self.emotion_value > 0:
            return -1 / (1 + math.exp(-self.k * self.emotion_value))
        return self.emotion_value

    def get_transformed_emotion(self) -> float:
        """Return emotion transformed toward its current polarity."""
        if self.emotion_value > 0:
            return self.transform_positive()
        if self.emotion_value < 0:
            return self.transform_negative()
        return 0.0
