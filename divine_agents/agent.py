"""Ontological agents and helper structures."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class ExtraSymbolicBox:
    """Fallback container that stores a stage and additional data."""

    stage: str
    data: Dict[str, Any] = field(default_factory=dict)
    protection: bool = False

    def update(self, stage: Optional[str] = None, **new_data: Any) -> None:
        if self.protection:
            raise PermissionError("Box is protected. Cannot update.")
        if stage:
            self.stage = stage
        self.data.update(new_data)


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history: List[str] = [state]
        # fallback box keeps the last stable state and metrics
        self.extra_box = ExtraSymbolicBox(stage=state, data={"tension": tension, "emotion": emotion})

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.extra_box.update(emotion=value, tension=self.tension)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.extra_box.update(tension=value)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            previous = self.state
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            self.extra_box.update(stage=self.state, previous_state=previous)
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            return f"{base} (čustveni odziv: {self.emotion:.1f})"
        return base

    def __str__(self) -> str:
        return f"{self.name} [{self.state}]"
