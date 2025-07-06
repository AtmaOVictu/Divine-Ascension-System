from __future__ import annotations

from .agent import Agent


class TypingAgent(Agent):
    """Agent that increases tension while typing words."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.words_typed: list[str] = []

    def type_word(self, word: str, emotion: float = 0.0) -> str:
        """Type a word, adjusting emotion and tension, and return a response."""
        self.words_typed.append(word)
        self.update_emotion(emotion)
        self.update_tension(0.1)
        self.transition()
        return self.respond_to_word(word)

    def respond_to_word(self, word: str) -> str:
        """Return a philosophical response based on the current state."""
        if self.state == "Ego":
            return f"{self.name} (Ego): Beseda '{word}' je absolutna resnica."
        if self.state == "Jaz":
            return f"{self.name} (Jaz): Beseda '{word}' ima relativni pomen."
        return f"{self.name} (Enotnost): Beseda '{word}' je del celovite resnice."
