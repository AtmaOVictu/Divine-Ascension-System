"""Core definitions for ontological agents."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Emotion:
    """Represents an emotional state with a certain intensity."""

    name: str
    intensity: float = 0.0


class Agent:
    """Ontological agent capable of moving through philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: Optional[Emotion] = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion or Emotion("nevtralno", 0.0)
        self.history: List[str] = [state]

    # ------------------------------------------------------------------
    # Emotion and tension handling
    # ------------------------------------------------------------------
    def update_emotion(self, intensity: float, name: Optional[str] = None) -> None:
        """Update the agent's emotional state and adjust tension."""

        if name:
            self.emotion.name = name
        self.emotion.intensity = intensity
        # Emotions raise overall tension which may trigger transitions
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set the agent's tension level."""

        self.tension = value

    # ------------------------------------------------------------------
    # State management
    # ------------------------------------------------------------------
    def transition(self) -> str:
        """Transition to the next philosophical state when thresholds are met."""

        if self.tension > 0.7 or self.emotion.intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    # ------------------------------------------------------------------
    # Dialogue helpers
    # ------------------------------------------------------------------
    def respond(self, question: str) -> str:
        """Return a philosophical response according to the current state."""

        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

