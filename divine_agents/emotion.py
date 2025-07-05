from math import exp

class EmotionTransformer:
    """Transform emotion values using a sigmoidal function."""

    def __init__(self, emotion_value: float, k: float = 1.0) -> None:
        self.emotion_value = emotion_value
        self.k = k

    def transform_positive(self) -> float:
        """Transform negative emotion toward the positive spectrum."""
        if self.emotion_value < 0:
            return 1 / (1 + exp(-self.k * self.emotion_value))
        return self.emotion_value

    def transform_negative(self) -> float:
        """Transform positive emotion toward the negative spectrum."""
        if self.emotion_value > 0:
            return -1 / (1 + exp(-self.k * self.emotion_value))
        return self.emotion_value

    def get_transformed_emotion(self) -> float:
        """Return emotion transformed toward the opposite range."""
        if self.emotion_value > 0:
            return self.transform_positive()
        elif self.emotion_value < 0:
            return self.transform_negative()
        return 0.0
