from __future__ import annotations

import time
from typing import Any, Dict

from .memory import Memory
from .utils import analyze_concept, calculate_tension_change


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.memory = Memory()

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
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    # --- New utility methods -------------------------------------------------
    def parse_philosophical_statement(self, statement: str) -> Dict[str, Any]:
        """Parse a philosophical statement and store it for reflection."""
        parsed = analyze_concept(statement)
        self.memory.store_long_term({"concept": parsed, "timestamp": time.time()})
        return parsed

    def simulate_emotional_tension(self, duration: int) -> float:
        """Simulate change in tension over a period of time."""
        final_tension = calculate_tension_change(self.tension, duration)
        self.memory.store_short_term({"emotion": self.emotion, "final_tension": final_tension, "duration": duration})
        self.tension = final_tension
        return final_tension

    def handle_complex_query(self, query: str) -> str:
        """Handle a simple complex query by delegating to internal tools."""
        if "emotion" in query:
            self.simulate_emotional_tension(duration=5)
            return f"{self.name} tension adjusted to {self.tension:.2f}"
        if "history" in query:
            return str(self.history)
        return "Query not understood"

    def self_reflection(self) -> str:
        """Reflect on past interactions to compute improvements."""
        interactions = self.memory.recall("long")
        improvements = len(interactions)
        return f"Self-reflection complete. Improvements identified: {improvements}"
