"""Base implementation of an ontological agent.

The agent can transition between three philosophical states based on
its emotion and tension.  Transitions occur when either the tension
exceeds ``0.7`` or the emotion exceeds ``0.5``.  The agent maintains a
history of visited states which can be inspected for debugging or
analysis.
"""

from dataclasses import dataclass, field
import uuid
from typing import List


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    uid: uuid.UUID = field(default_factory=uuid.uuid4, init=False)
    history: List[str] = field(default_factory=lambda: ["Ego"], init=False)

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and increase tension accordingly."""
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
        base = ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} {self._emotion_phrase()}"

    def _emotion_phrase(self) -> str:
        """Return a short phrase describing the agent's emotional state."""
        if self.emotion > 0.7:
            return "Čutim intenzivna čustva."  # strong emotion
        if self.emotion > 0.3:
            return "Moja čustva vplivajo na moje dojemanje."  # mild emotion
        return "Sem miren."  # low emotion
