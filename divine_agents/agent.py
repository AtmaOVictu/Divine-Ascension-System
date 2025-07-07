from typing import Dict


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        mood: str = "neutral",
        language: str = "en",
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.mood = mood
        self.language = language
        self.history = [state]

    # ------------------------------------------------------------------
    # Emotion Handling
    # ------------------------------------------------------------------
    def update_emotion(self, mood: str, value: float, language: str | None = None) -> str:
        """Update emotion intensity and adjust tension based on emotion type."""
        self.mood = mood
        self.emotion = value
        if mood in ("fear", "anger"):
            self.tension += value
        elif mood == "joy":
            self.tension -= value
        else:
            self.tension += value / 2
        lang = language or self.language
        return self._emotion_response(mood, lang)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    # ------------------------------------------------------------------
    # Transitions
    # ------------------------------------------------------------------
    def dynamic_threshold(self, kind: str) -> float:
        """Return threshold for the given attribute based on current mood."""
        base = 0.7 if kind == "tension" else 0.5
        if self.mood == "anger":
            return base * 0.8  # lower threshold when angry
        return base

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > self.dynamic_threshold("tension") or self.emotion > self.dynamic_threshold("emotion"):
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def log_transition(self) -> str:
        """Return a textual log describing the latest transition."""
        if self.state == "Jaz":
            return f"{self.name} transitioned to Jaz due to high tension or emotion."
        if self.state == "Enotnost":
            return f"{self.name} reached Enotnost, achieving unity."
        return ""

    # ------------------------------------------------------------------
    # Responses
    # ------------------------------------------------------------------
    def respond(self, question: str, language: str | None = None) -> str:
        """Return a philosophical answer depending on the current state and language."""
        lang = language or self.language
        responses: Dict[str, Dict[str, str]] = {
            "Ego": {
                "en": "Truth is absolute and independent of others.",
                "sl": "Resnica je absolutna in neodvisna od drugih.",
            },
            "Jaz": {
                "en": "Truth is relative, shaped by our relationships.",
                "sl": "Resnica je relativna, oblikovana z našimi odnosi.",
            },
            "Enotnost": {
                "en": "All truths are one, interconnected.",
                "sl": "Vse resnice so eno, medsebojno povezane.",
            },
        }
        return responses[self.state].get(lang, responses[self.state]["en"])

    def _emotion_response(self, mood: str, language: str) -> str:
        responses: Dict[str, Dict[str, str]] = {
            "anger": {"en": "I feel a rising anger.", "sl": "Čutim naraščajočo jezo."},
            "fear": {"en": "I feel scared.", "sl": "Čutim strah."},
            "joy": {"en": "I feel happy.", "sl": "Čutim veselje."},
        }
        return responses.get(mood, {}).get(language, "I feel a complex emotion.")
