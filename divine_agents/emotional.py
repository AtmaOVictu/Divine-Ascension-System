from .agent import Agent

class EmotionalAgent(Agent):
    """Agent capable of processing and validating emotions."""

    def process_emotion(self, emotion: str) -> str:
        if emotion in ["anger", "frustration"]:
            return "Emotion confirmed: Negative"
        if emotion in ["happiness", "joy"]:
            return "Emotion confirmed: Positive"
        return "Emotion confirmed: Neutral"
