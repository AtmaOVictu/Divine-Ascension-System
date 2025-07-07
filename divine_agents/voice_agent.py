from .agent import Agent

class VoiceAgent(Agent):
    """Voice agent capable of emotional interaction and state transitions."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, mood: str = "neutral"):
        super().__init__(name, state, tension, emotion)
        self.mood = mood

    def update_emotion(self, mood: str, value: float) -> None:
        """Update emotion intensity and adjust tension based on emotion type."""
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
        """Return response based on mood, state, and emotional context."""
        base = super().respond(question)
        tone = self._determine_tone()
        return f"{base}{tone}"

    def _determine_tone(self) -> str:
        mapping = {
            "anger": " (spoken with anger)",
            "fear": " (spoken with fear)",
            "joy": " (spoken with joy)",
            "neutral": " (spoken neutrally)",
        }
        return mapping.get(self.mood, "")
