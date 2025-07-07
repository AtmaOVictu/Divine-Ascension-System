"""Emotion handling for ontological agents."""

class EmotionalAgent:
    """Agent dedicated to processing and confirming emotional states."""

    def __init__(self):
        self.name = "Emotional Agent"

    def process_emotion(self, emotion: str) -> str:
        """Return a confirmation string based on the emotion provided."""
        if emotion in {"anger", "fear"}:
            return "Emotion confirmed: Negative"
        if emotion in {"joy"}:
            return "Emotion confirmed: Positive"
        return "Emotion confirmed: Neutral"


class EmotionalBox:
    """Container for holding emotion before confirmation."""

    def __init__(self, emotion: str):
        self.emotion = emotion
        self.status = "unprocessed"

    def process(self, emotional_agent: EmotionalAgent) -> str:
        """Process the stored emotion and update status."""
        self.status = emotional_agent.process_emotion(self.emotion)
        return self.status
