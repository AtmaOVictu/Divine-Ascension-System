import math

class EmotionTransformer:
    """Utility to mutate emotion values within [-1, 1] using sigmoidal rules."""

    def __init__(self, emotion_value: float, k: float = 1.0):
        self.emotion_value = emotion_value
        self.k = k

    def transform_positive(self) -> float:
        """Transform emotion value within the positive spectrum (0 to 1)."""
        if self.emotion_value > 0:
            return 1 / (1 + math.exp(-self.k * self.emotion_value))
        return self.emotion_value

    def transform_negative(self) -> float:
        """Transform emotion value within the negative spectrum (-1 to 0)."""
        if self.emotion_value < 0:
            return -1 / (1 + math.exp(-self.k * self.emotion_value))
        return self.emotion_value

    def get_transformed_emotion(self) -> float:
        """Return the transformed emotion based on its sign."""
        if self.emotion_value > 0:
            return self.transform_positive()
        if self.emotion_value < 0:
            return self.transform_negative()
        return 0.0
