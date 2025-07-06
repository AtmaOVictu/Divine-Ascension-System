"""Ontological agents capable of philosophical state transitions."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Agent:
    """Represent an agent that can move through ontological states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_name: str = "neutral"
    key: Optional[str] = None
    history: List[str] = field(default_factory=list)

    #: Mapping of activation keys to ontological states
    ACTIVATION_MAP: Dict[str, str] = field(
        default_factory=lambda: {
            "truth": "Ego",
            "negation": "Jaz",
            "wisdom": "Enotnost",
        }
    )

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def update_emotion(self, value: float, name: str = "neutral") -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.emotion_name = name
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

    def set_key(self, key: str) -> None:
        """Activate a state change based on a symbolic key."""
        self.key = key
        self.state = self.ACTIVATION_MAP.get(key, self.state)
        self.history.append(self.state)

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by ontological state."""
        emotion_note = (
            "mirno" if self.emotion <= 0.5 else f"v čustvu {self.emotion_name}"
        )

        if self.state == "Ego":
            answer = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            answer = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            answer = "Vse resnice so eno, medsebojno povezane."
        return f"{self.name} ({self.state}, {emotion_note}): {answer}"
