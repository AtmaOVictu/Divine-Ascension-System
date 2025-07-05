class EmotionTransformer:
    """Transform emotion values between negative and positive ranges."""

    def __init__(self, emotion_value: float, k: float = 1.0):
        self.emotion_value = emotion_value
        self.k = k

    def transform_positive(self) -> float:
        """Transform negative emotion into a positive range using a sigmoid."""
        if self.emotion_value < 0:
            return 1 / (1 + (__import__('math').exp(-self.k * self.emotion_value)))
        return self.emotion_value

    def transform_negative(self) -> float:
        """Transform positive emotion into a negative range using a sigmoid."""
        if self.emotion_value > 0:
            return -1 / (1 + (__import__('math').exp(-self.k * self.emotion_value)))
        return self.emotion_value

    def get_transformed_emotion(self) -> float:
        """Return the transformed emotion based on its sign."""
        if self.emotion_value > 0:
            return self.transform_negative()
        if self.emotion_value < 0:
            return self.transform_positive()
        return 0.0
