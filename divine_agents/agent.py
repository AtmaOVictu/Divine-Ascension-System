from enum import Enum


class OntologyState(Enum):
    """Enumeration of possible ontological states."""

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
        self.history = [state]
        self.new_boxes = []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = min(1.0, max(0.0, value))
        self.tension = min(1.0, max(0.0, self.tension + self.emotion))
        self._check_extremes()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = min(1.0, max(0.0, value))
        self._check_extremes()

    def transition(self) -> OntologyState:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == OntologyState.EGO:
                self.state = OntologyState.JAZ
            elif self.state == OntologyState.JAZ:
                self.state = OntologyState.ENOTNOST
        self.history.append(self.state)
        return self.state

    def _check_extremes(self) -> None:
        """Create boxes when emotion or tension hit extreme levels."""
        if self.tension > 0.8:
            self.create_new_box("High Tension Box")
        elif self.tension < 0.2:
            self.create_new_box("Low Tension Box")
        if self.emotion > 0.8:
            self.create_new_box("Extreme Emotion Box")
        elif self.emotion < 0.2:
            self.create_new_box("Calm Emotion Box")

    def create_new_box(self, name: str) -> None:
        """Record a new ontological box when extremes occur."""
        if name not in self.new_boxes:
            self.new_boxes.append(name)

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == OntologyState.EGO:
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == OntologyState.JAZ:
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
