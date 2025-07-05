from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from .enums import EmotionType, OntologicalState


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: OntologicalState = OntologicalState.EGO
    tension: float = 0.0
    emotion_intensity: float = 0.0
    emotion_type: EmotionType = EmotionType.NEUTRAL
    history: List[OntologicalState] = field(default_factory=lambda: [OntologicalState.EGO])

    def feel(self, emotion: EmotionType, intensity: float) -> None:
        """Set the agent's emotion and adjust tension."""
        self.emotion_type = emotion
        self.emotion_intensity = intensity
        self.tension += intensity

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity neutrally and adjust tension."""
        self.feel(EmotionType.NEUTRAL, value)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> OntologicalState:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_intensity > 0.5:
            if self.state == OntologicalState.EGO:
                self.state = OntologicalState.JAZ
            elif self.state == OntologicalState.JAZ:
                self.state = OntologicalState.ENOTNOST
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == OntologicalState.EGO:
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == OntologicalState.JAZ:
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        emotion_prefix = {
            EmotionType.FEAR: "S strahom, ",
            EmotionType.JOY: "Z veseljem, ",
            EmotionType.ANGER: "Z jezo, ",
        }.get(self.emotion_type, "")
        return f"{emotion_prefix}{base}"
