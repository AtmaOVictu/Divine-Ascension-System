class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, mood: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.mood = mood
        self.history = [state]

    def update_emotion(self, mood: str, value: float, language: str = "sl") -> None:
        """Update emotion intensity, mood and adjust tension accordingly."""
        self.mood = mood
        self.emotion = value
        if mood in ("fear", "anger"):
            self.tension += value
        elif mood == "joy":
            self.tension -= value
        else:
            self.tension += value / 2
        print(self._emotion_response(mood, language))

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

    def respond(self, question: str, language: str = "sl") -> str:
        """Return a philosophical answer depending on the current state."""
        responses = {
            "Ego": {
                "en": "Truth is absolute and independent of others.",
                "sl": "Resnica je absolutna in neodvisna od drugih.",
            },
            "Jaz": {
                "en": "Truth is relative, shaped by our relationships.",
                "sl": "Resnica je relativna, oblikovana z našimi odnosi.",
            },
            "Enotnost": {
                "en": "All truths are one and interconnected.",
                "sl": "Vse resnice so eno, medsebojno povezane.",
            },
        }
        return responses[self.state].get(language, responses[self.state]["en"])

    def _emotion_response(self, mood: str, language: str) -> str:
        """Return a language-specific message for the given mood."""
        responses = {
            "anger": {"en": "I feel a rising anger.", "sl": "\u010cutim nara\u0161\u010dajo\u010do jezo."},
            "fear": {"en": "I feel scared.", "sl": "\u010cutim strah."},
            "joy": {"en": "I feel happy.", "sl": "\u010cutim veselje."},
        }
        return responses.get(mood, {}).get(language, "I feel a complex emotion.")
