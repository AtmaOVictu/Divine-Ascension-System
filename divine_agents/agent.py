from datetime import datetime
from typing import Optional, Dict, List


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history: List[Dict[str, object]] = []
        self.log_transition(None, state, tension, emotion, notes="initial")

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        prev_state = self.state
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"

        if self.state != prev_state:
            self.log_transition(prev_state, self.state, self.tension, self.emotion)
        return self.state

    def log_transition(
        self,
        prev_state: Optional[str],
        new_state: str,
        tension: float,
        emotion: float,
        notes: Optional[str] = None,
    ) -> None:
        """Record a state change entry with timestamp."""
        entry = {
            "timestamp": datetime.utcnow(),
            "from": prev_state,
            "to": new_state,
            "tension": tension,
            "emotion": emotion,
            "notes": notes,
        }
        self.history.append(entry)

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
