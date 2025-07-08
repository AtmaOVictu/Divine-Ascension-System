import time
from typing import List, Dict
from .dictionary import OntologicalDictionary


class WritingAgent:
    """Agent responsible for writing events and reflections."""

    def __init__(self, name: str):
        self.name = name
        self.transcription_history: List[Dict] = []

    def write_event(self, event: str, emotional_state: str, philosophical_reflection: str) -> None:
        entry = {
            "event": event,
            "emotional_state": emotional_state,
            "philosophical_reflection": philosophical_reflection,
            "timestamp": time.time(),
        }
        self.transcription_history.append(entry)

    def review_history(self) -> List[Dict]:
        return self.transcription_history

    def summarize_journey(self) -> str:
        summary = ""
        for entry in self.transcription_history:
            summary += (
                f"Event: {entry['event']}, Emotional State: {entry['emotional_state']}, "
                f"Reflection: {entry['philosophical_reflection']}\n"
            )
        return summary


class ReflectiveWritingAgent(WritingAgent):
    """Agent that writes reflections using an ontological dictionary."""

    def __init__(self, name: str, dictionary: OntologicalDictionary):
        super().__init__(name)
        self.dictionary = dictionary

    def reflect_and_write(self, event: str, emotional_state: str, philosophical_input: str) -> None:
        meaning = self.dictionary.get_word_meaning(emotional_state)
        emotional_intensity = meaning["emotional_intensity"]
        reflection = f"Reflection on {event}: {philosophical_input}."
        self.write_event(event, emotional_state, reflection)
        # store intensity for reference
        self.transcription_history[-1]["emotional_intensity"] = emotional_intensity
