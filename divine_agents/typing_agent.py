from __future__ import annotations

from .agent import Agent


class TypingAgent(Agent):
    """Agent that changes state while typing words."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.words_typed: list[str] = []

    def update_emotion(self, value: float) -> None:  # type: ignore[override]
        """Increment emotion and tension."""
        self.emotion += value
        self.tension += value

    def type_word(self, word: str, emotion_delta: float = 0.0) -> str:
        """Type a word and possibly transition ontological state."""
        self.words_typed.append(word)
        # Each word increases tension slightly
        self.update_tension(self.tension + 0.1)
        if emotion_delta:
            self.update_emotion(emotion_delta)
        # transition if thresholds reached
        self.transition()
        return self.respond_to_word(word)

    def respond_to_word(self, word: str) -> str:
        """Return a philosophical response to a word, influenced by emotion."""
        base = ""
        if self.state == "Ego":
            base = f"Beseda '{word}' je absolutna resnica."
        elif self.state == "Jaz":
            base = f"Beseda '{word}' ima relativni pomen."
        else:
            base = f"Beseda '{word}' je del celovite resnice."
        if self.emotion > 0.5:
            base += " Čutim močna čustva."
        return f"{self.name} ({self.state}): {base}"
