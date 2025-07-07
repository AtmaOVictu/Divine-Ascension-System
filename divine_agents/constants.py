class Constants:
    """Holds threshold values for agent state transitions."""

    EMOTION_THRESHOLD = 0.5
    TENSION_THRESHOLD = 0.7
    MAX_EMOTION = 1.0
    MIN_EMOTION = 0.0

    @staticmethod
    def emotion_high(value: float) -> bool:
        return value > Constants.EMOTION_THRESHOLD

    @staticmethod
    def tension_high(value: float) -> bool:
        return value > Constants.TENSION_THRESHOLD
