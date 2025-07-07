class EmotionalAgent:
    """Simple emotional agent to validate emotions."""

    def process_emotion(self, emotion: str) -> str:
        if emotion.lower() in {"anger", "fear", "frustration"}:
            return "Emotion confirmed: Negative"
        if emotion.lower() in {"joy", "happiness", "delight"}:
            return "Emotion confirmed: Positive"
        return "Emotion confirmed: Neutral"
