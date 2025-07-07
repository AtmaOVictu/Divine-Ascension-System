from enum import Enum

class EmotionType(Enum):
    NEUTRAL = "neutral"
    FEAR = "fear"
    JOY = "joy"
    ANGER = "anger"

# Multipliers for how each emotion influences tension
EMOTION_TENSION_FACTOR = {
    EmotionType.NEUTRAL: 0.0,
    EmotionType.FEAR: 0.6,
    EmotionType.JOY: 0.4,
    EmotionType.ANGER: 0.7,
}
