from .emotion import EmotionalBox


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    RESPONSES = {
        "English": {
            "Ego": "Truth is absolute and independent of others.",
            "Jaz": "Truth is relative and shaped by our relationships.",
            "Enotnost": "All truths are one, interconnected.",
        },
        "Spanish": {
            "Ego": "La verdad es absoluta e independiente de los dem\u00e1s.",
            "Jaz": "La verdad es relativa y se forma con nuestras relaciones.",
            "Enotnost": "Todas las verdades son una, interconectadas.",
        },
        "German": {
            "Ego": "Die Wahrheit ist absolut und von anderen unabh\u00e4ngig.",
            "Jaz": "Die Wahrheit ist relativ und wird durch Beziehungen geformt.",
            "Enotnost": "Alle Wahrheiten sind eins und miteinander verbunden.",
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

    def evolve(self) -> str:
        """Update emotional state via EmotionalBox and attempt transition."""
        self.emotional_box.language = self.language
        self.emotional_box.update_emotion()
        return self.transition()

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
        """Return a philosophical answer depending on the current state and language."""
        responses = self.RESPONSES.get(self.language, self.RESPONSES["English"])
        return responses.get(self.state, "")
