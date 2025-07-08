from __future__ import annotations

from typing import List, Optional


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, shared_memory: Optional["SharedMemory"] = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.shared_memory = shared_memory

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

    def reflect(self) -> str:
        """Create a reflection about the current state and store it."""
        reflection = f"{self.name} reflects while in {self.state}."
        if self.shared_memory:
            self.shared_memory.record_event(reflection)
        return reflection

    def learn_from_memory(self, history: List[str]) -> None:
        """Adjust emotion based on shared memory and trigger transitions."""
        for event in history:
            if "conflict" in event:
                self.update_emotion(0.8)
            elif "peace" in event:
                self.update_emotion(0.2)
        self.transition()

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
