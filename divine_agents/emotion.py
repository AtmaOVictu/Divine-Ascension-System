import math

class EmotionTransformer:
    """Perform simple emotion transformations using a sigmoid."""

    def __init__(self, emotion_value: float, k: float = 1.0) -> None:
        self.emotion_value = emotion_value
        self.k = k

    def transform(self) -> float:
        """Transform emotion to the opposite spectrum."""
        if self.emotion_value < 0:
            return 1 / (1 + math.exp(-self.k * self.emotion_value))
        if self.emotion_value > 0:
            return -1 / (1 + math.exp(-self.k * self.emotion_value))
        return 0.0
