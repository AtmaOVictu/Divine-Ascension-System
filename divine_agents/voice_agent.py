from .agent import Agent


class VoiceAgent(Agent):
    """Voice agent with emotional context and tone."""

    def __init__(self, name: str, state: str = "Ego", emotion: float = 0.0, mood: str = "neutral"):
        super().__init__(name, state, tension=0.0, emotion=emotion)
        self.mood = mood

    def update_emotion(self, mood: str, value: float) -> None:
        """Update emotion intensity and adjust tension based on the mood."""
        self.mood = mood
        self.emotion = value
        if mood == "anger":
            self.tension += value
        elif mood == "joy":
            self.tension -= value
        elif mood == "fear":
            self.tension += value * 1.5
        else:
            self.tension += value / 2

    def respond(self, question: str) -> str:
        """Return response influenced by current ontological and emotional state."""
        base = super().respond(question)
        tone = self._determine_tone()
        return base + tone

    def _determine_tone(self) -> str:
        tone_mapping = {
            "anger": " (spoken with anger)",
            "fear": " (spoken with fear)",
            "joy": " (spoken with joy)",
            "neutral": " (spoken neutrally)",
        }
        return tone_mapping.get(self.mood, "")
