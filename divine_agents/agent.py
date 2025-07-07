"""Ontological agent capable of transitioning between philosophical states."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Represents an ontological agent with emotional and tension states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_type: str = "neutral"
    history: List[str] = field(default_factory=list)

    # Thresholds that trigger state transitions
    THRESHOLD_TENSION = 0.7
    THRESHOLD_EMOTION = 0.5

    STATES = ("Ego", "Jaz", "Enotnost")

    def __post_init__(self) -> None:
        self.history.append(self.state)

    # ------------------------------------------------------------------
    # Emotion and tension updates
    # ------------------------------------------------------------------
    def update_emotion(self, emotion_type: str, intensity: float) -> None:
        """Update emotion type and intensity while adjusting tension."""
        self.emotion_type = emotion_type
        self.emotion = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    # ------------------------------------------------------------------
    # State management
    # ------------------------------------------------------------------
    def transition(self) -> str:
        """Perform a state transition if emotion or tension exceed thresholds."""
        if self.tension > self.THRESHOLD_TENSION or self.emotion > self.THRESHOLD_EMOTION:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    # ------------------------------------------------------------------
    # Dialogue handling
    # ------------------------------------------------------------------
    def respond(self) -> str:
        """Return a philosophical response influenced by current state and emotion."""
        if self.state == "Ego":
            return (
                f"Z občutkom {self.emotion_type} trdim, da je resnica absolutna in neodvisna od drugih."
            )
        if self.state == "Jaz":
            return (
                f"V duhu {self.emotion_type} menim, da je resnica relativna, oblikovana z našimi odnosi."
            )
        return (
            f"Prežet z {self.emotion_type} vidim, da so vse resnice eno in medsebojno povezane."
        )
