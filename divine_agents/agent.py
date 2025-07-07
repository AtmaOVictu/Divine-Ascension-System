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

    def update_emotion(self, mood: str, value: float, language: str = "en") -> None:
        """Update emotion intensity and adjust tension based on emotion type."""
        self.mood = mood
        self.emotion = value
        response = ""
        if mood in ("fear", "anger"):
            self.tension += value
            response = self._emotion_response("anger", language)
        elif mood == "joy":
            self.tension -= value
            response = self._emotion_response("joy", language)
        else:
            self.tension += value / 2
        print(response)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Transition dynamically based on emotion and tension."""
        if self.tension > self.dynamic_threshold("tension") or self.emotion > self.dynamic_threshold("emotion"):
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def dynamic_threshold(self, type: str) -> float:
        """Dynamically adjust thresholds based on emotion or tension type."""
        base_threshold = 0.7 if type == "tension" else 0.5
        if self.mood == "anger":
            return base_threshold * 0.8
        return base_threshold

    def respond(self, question: str, language: str = "en") -> str:
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

    def _emotion_response(self, mood: str, language: str):
        responses = {
            "anger": {
                "en": "I feel a rising anger.",
                "sl": "Čutim naraščajočo jezo.",
            },
            "fear": {
                "en": "I feel scared.",
                "sl": "Čutim strah.",
            },
            "joy": {
                "en": "I feel happy.",
                "sl": "Čutim veselje.",
            },
        }
        return responses.get(mood, {}).get(language, "I feel a complex emotion.")

    def log_transition(self) -> str:
        if self.state == "Jaz":
            return f"{self.name} transitioned to Jaz due to high tension or emotion."
        if self.state == "Enotnost":
            return f"{self.name} reached Enotnost, achieving unity."
        return ""
