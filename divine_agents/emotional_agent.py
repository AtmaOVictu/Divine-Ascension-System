from .agent import Agent


class EmotionalAgent(Agent):
    """Agent with discrete emotions influencing tension."""

    EMOTION_EFFECTS = {
        "fear": 0.4,
        "anger": 0.6,
        "joy": 0.2,
        "sorrow": 0.5,
    }

    def feel(self, emotion: str) -> None:
        """Apply an emotion to the agent, adjusting emotion intensity and tension."""
        intensity = self.EMOTION_EFFECTS.get(emotion, 0.0)
        self.update_emotion(intensity)

    def philosophy(self, question: str) -> str:
        """Return a philosophical answer considering the current emotional state."""
        reply = self.respond(question)
        if self.emotion > 0.5:
            reply += " Čutim močna čustva."  # Emotional note
        return reply
