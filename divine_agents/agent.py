"""Core agent logic used across the project."""

from dataclasses import dataclass, field
from typing import List, Optional

from .ontology import OntologyState, STATE_SYMBOLS


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = OntologyState.EGO.value
    tension: float = 0.0
    emotion: float = 0.0
    emotion_type: Optional[str] = None
    history: List[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def update_emotion(self, value: float, emotion_type: Optional[str] = None) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        if emotion_type:
            self.emotion_type = emotion_type
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == OntologyState.EGO.value:
                self.state = OntologyState.JAZ.value
            elif self.state == OntologyState.JAZ.value:
                self.state = OntologyState.ENOTNOST.value
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        base: str
        if self.state == OntologyState.EGO.value:
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == OntologyState.JAZ.value:
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_type:
            return f"{self.emotion_type.capitalize()} me vodi k misli, da {base}"
        return base

    def symbol(self) -> str:
        """Return ontological symbol representing the current state."""
        for key, value in STATE_SYMBOLS.items():
            if key.value == self.state:
                return value
        return ""
