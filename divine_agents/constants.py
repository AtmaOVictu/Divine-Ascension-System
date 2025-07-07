class Constants:
    """Constant values governing agent behaviour."""
    EMOTION_THRESHOLD = 0.5
    TENSION_THRESHOLD = 0.7
    MAX_EMOTION = 1.0
    MIN_EMOTION = 0.0

    @staticmethod
    def is_emotion_high(value: float) -> bool:
        return value >= Constants.EMOTION_THRESHOLD

    @staticmethod
    def is_tension_high(value: float) -> bool:
        return value >= Constants.TENSION_THRESHOLD

