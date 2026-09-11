from enum import Enum
from typing import List


class OntologyState(Enum):
    """Enumeration of possible ontological states for an agent."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    def __init__(self, name: str, state: OntologyState = OntologyState.EGO,
                 tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history: List[OntologyState] = [state]
        self.new_boxes: List[str] = []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Values are clamped between 0.0 and 1.0. Extreme values create new
        ontological boxes."""
        self.emotion = max(0.0, min(1.0, value))
        if self.emotion > 0.8:
            self.create_new_box("Extreme Emotion Box")
        if self.emotion < 0.2:
            self.create_new_box("Calm Emotion Box")
        self.tension = max(0.0, min(1.0, self.tension + self.emotion))

    def update_tension(self, value: float) -> None:
        """Directly set tension level.

        The value is clamped between 0.0 and 1.0 and may create new boxes
        if it represents an extreme."""
        self.tension = max(0.0, min(1.0, value))
        if self.tension > 0.8:
            self.create_new_box("High Tension Box")
        if self.tension < 0.2:
            self.create_new_box("Low Tension Box")

    def transition(self) -> OntologyState:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == OntologyState.EGO:
                self.state = OntologyState.JAZ
            elif self.state == OntologyState.JAZ:
                self.state = OntologyState.ENOTNOST
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == OntologyState.EGO:
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == OntologyState.JAZ:
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def create_new_box(self, box_name: str) -> None:
        """Record entry into a new ontological box."""
        self.new_boxes.append(box_name)
