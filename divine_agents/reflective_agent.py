from typing import Optional
from .agent import Agent
from .dictionary import OntologicalDictionary
from .writer import WritingAgent


class ReflectiveAgent(Agent):
    """Agent capable of reflective writing using an ontological dictionary."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, dictionary: Optional[OntologicalDictionary] = None, writer: Optional[WritingAgent] = None):
        super().__init__(name, state, tension, emotion)
        self.dictionary = dictionary or OntologicalDictionary()
        self.writer = writer or WritingAgent(name)

    def reflect_and_write(self, event: str, emotional_word: str, philosophical_input: str) -> None:
        """Reflect on an event and record it with emotional context."""
        meaning = self.dictionary.get_word_meaning(emotional_word)
        intensity = meaning["emotional_intensity"]
        self.update_emotion(intensity / 10)
        self.transition()
        reflection = f"Reflection on {event}: {philosophical_input}"
        self.writer.write_event(event, emotional_word, reflection)
