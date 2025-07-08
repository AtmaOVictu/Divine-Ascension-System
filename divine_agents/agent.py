from enum import Enum


class OntologyState(Enum):
    """Enumeration of possible ontological states for an agent."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    def __init__(self, name: str, state: OntologyState = OntologyState.EGO, tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.new_boxes = []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = max(0.0, min(1.0, value))
        self.tension = max(0.0, min(1.0, self.tension + self.emotion))
        if self.emotion > 0.8:
            self.create_new_box("Extreme Emotion Box")
        elif self.emotion < 0.2:
            self.create_new_box("Calm Emotion Box")

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, min(1.0, value))
        if self.tension > 0.8:
            self.create_new_box("High Tension Box")
        elif self.tension < 0.2:
            self.create_new_box("Low Tension Box")

    def create_new_box(self, name: str) -> None:
        """Record the creation of a new box when extremes are reached."""
        self.new_boxes.append(name)

    def transition(self) -> str:
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
