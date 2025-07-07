class EmotionalAgent:
    """Agent responsible for validating emotions."""

    def __init__(self, name: str = "Emotional Agent"):
        self.name = name

    def process_emotion(self, emotion: str) -> str:
        """Return a confirmation string based on the emotion value."""
        negative = {"anger", "frustration", "fear"}
        positive = {"happiness", "joy"}
        if emotion in negative:
            return "Emotion confirmed: Negative"
        if emotion in positive:
            return "Emotion confirmed: Positive"
        return "Emotion confirmed: Neutral"
