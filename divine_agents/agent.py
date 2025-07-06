"""Basic ontological agent implementation used in tests and simulations."""

from typing import Dict, List


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotions: Dict[str, float] | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions: Dict[str, float] = emotions or {"fear": 0.0, "joy": 0.0, "anger": 0.0}
        self.history: List[str] = [state]

    # ------------------------------------------------------------------
    # Emotion and tension handling
    # ------------------------------------------------------------------
    def emotional_intensity(self) -> float:
        """Return the highest intensity among stored emotions."""
        return max(self.emotions.values(), default=0.0)

    def update_emotion(self, name: str, value: float) -> None:
        """Set a specific emotion and adjust tension accordingly."""
        self.emotions[name] = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    # ------------------------------------------------------------------
    # State management
    # ------------------------------------------------------------------
    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotional_intensity() > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    # ------------------------------------------------------------------
    # Dialogue helpers
    # ------------------------------------------------------------------
    def _describe_emotion(self) -> str:
        mood = max(self.emotions, key=self.emotions.get, default=None)
        if mood and self.emotions[mood] > 0:
            return f"Čustvo {mood} ({self.emotions[mood]:.2f})."
        return ""

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna in oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        emotion = self._describe_emotion()
        return f"{base} {emotion}".strip()
