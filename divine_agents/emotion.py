class EmotionEffects:
    """Mapping of emotions to tension increments."""
    TENSION_MAP = {
        "fear": 0.6,
        "anger": 0.7,
        "joy": 0.4,
        "sorrow": 0.5,
    }


def apply_emotion(agent, emotion_name: str) -> None:
    """Apply an emotion to an agent and update their internal state."""
    value = EmotionEffects.TENSION_MAP.get(emotion_name, 0)
    agent.update_emotion(value)
