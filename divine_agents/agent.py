class Agent:
    """Ontological agent capable of emotional transitions between states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, mood: str = "neutral") -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.mood = mood
        self.history = [state]

    def update_emotion(self, mood: str, value: float) -> None:
        """Update emotion intensity and adjust tension based on mood."""
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

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on current ontological state."""
        base_response = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane."
        }
        tone = self._determine_tone()
        return base_response.get(self.state, "Neznano stanje") + tone

    def _determine_tone(self) -> str:
        mapping = {
            "anger": " (govorjeno z jezo)",
            "fear": " (govorjeno s strahom)",
            "joy": " (govorjeno z veseljem)",
            "neutral": ""
        }
        return mapping.get(self.mood, "")
