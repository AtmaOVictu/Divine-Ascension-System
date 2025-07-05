import math

class EmotionTransformer:
    """Transform emotions using a logistic approach between -1 and 1."""

    def __init__(self, emotion_value: float, k: float = 1.0) -> None:
        self.emotion_value = emotion_value
        self.k = k

    def transform_positive(self) -> float:
        """Transform negative emotion toward the positive range."""
        if self.emotion_value < 0:
            return 1 / (1 + math.exp(-self.k * self.emotion_value))
        return self.emotion_value

    def transform_negative(self) -> float:
        """Transform positive emotion toward the negative range."""
        if self.emotion_value > 0:
            return -1 / (1 + math.exp(-self.k * self.emotion_value))
        return self.emotion_value

    def get_transformed_emotion(self) -> float:
        """Return the transformed emotion based on its sign."""
        if self.emotion_value > 0:
            return self.transform_positive()
        if self.emotion_value < 0:
            return self.transform_negative()
        return 0.0
