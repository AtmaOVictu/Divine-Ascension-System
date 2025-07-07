from .agent import Agent

class VoiceAgent(Agent):
    """Voice agent interacting with emotional tension and transitions."""

    def __init__(self, name: str, state: str = "Ego", emotion: float = 0.0,
                 mood: str = "neutral", tension: float = 0.0):
        super().__init__(name, state=state, tension=tension, emotion=emotion)
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

    def transition(self) -> str:
        """Transition between states based on emotional tension."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            else:
                self.state = "Ego"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return response based on mood, state, and emotional context."""
        base_response = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane."
        }
        tone = self._determine_tone()
        return base_response.get(self.state, "Neznano") + tone

    def _determine_tone(self) -> str:
        """Determine the tone based on emotional state."""
        tone_mapping = {
            "anger": " (izrečeno z jezo)",
            "fear": " (izrečeno s strahom)",
            "joy": " (izrečeno z veseljem)",
            "neutral": " (izrečeno nevtralno)"
        }
        return tone_mapping.get(self.mood, "")
