from typing import Dict

from .emotion import EmotionalBox


class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    PHRASES: Dict[str, Dict[str, str]] = {
        "Ego": {
            "English": "Truth is absolute and independent of others.",
            "Spanish": "La verdad es absoluta e independiente de los dem\u00e1s.",
            "German": "Die Wahrheit ist absolut und unabh\u00e4ngig von anderen.",
        },
        "Jaz": {
            "English": "Truth is relative, shaped by our relationships.",
            "Spanish": "La verdad es relativa y se forma a trav\u00e9s de nuestras relaciones.",
            "German": "Wahrheit ist relativ und wird durch Beziehungen gestaltet.",
        },
        "Enotnost": {
            "English": "All truths are one and interconnected.",
            "Spanish": "Todas las verdades son una y est\u00e1n interconectadas.",
            "German": "Alle Wahrheiten sind eins und miteinander verbunden.",
        },
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, language: str = "English"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.language = language
        self.history = [state]
        self.emotional_box = EmotionalBox(self, language)

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

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
        """Return a philosophical answer depending on the current state."""
        return self.PHRASES[self.state][self.language]
