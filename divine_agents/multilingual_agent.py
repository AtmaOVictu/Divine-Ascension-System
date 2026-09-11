from .agent import Agent
from .emotion import EmotionalBox


class MultilingualAgent(Agent):
    """Agent aware of language-based emotions and responses."""

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
            "Enotnost": "Alle Wahrheiten sind eins und verbunden.",
        },
        "French": {
            "Ego": "La v\u00e9rit\u00e9 est absolue et ind\u00e9pendante des autres.",
            "Jaz": "La v\u00e9rit\u00e9 est relative et forgee par nos relations.",
            "Enotnost": "Toutes les v\u00e9rit\u00e9s sont une, interconnect\u00e9es.",
        },
    }

    def __init__(self, name: str, language: str = "English", state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state=state, tension=tension, emotion=emotion)
        self.language = language
        self.emotional_box = EmotionalBox(self, language)

    def respond(self, question: str) -> str:
        messages = self.RESPONSES.get(self.language, self.RESPONSES["English"])
        return messages.get(self.state, "")

    def evolve(self) -> str:
        """Update emotions via the emotional box and perform a transition."""
        self.emotional_box.update_emotion()
        return self.transition()
