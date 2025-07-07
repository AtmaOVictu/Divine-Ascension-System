from __future__ import annotations

import time
from typing import Optional

from .symbol import Symbol


class Agent:
    """Ontological agent capable of emotional transitions and responses."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_type: str = "neutral",
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.symbol = Symbol(name)
        self.history = [state]
        self.timestamp = time.time()

    def update_emotion(self, value: float, emotion_type: Optional[str] = None) -> None:
        """Update emotion intensity, type and adjust tension."""
        if emotion_type:
            self.emotion_type = emotion_type
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if emotion or tension exceed thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            self.symbol.evolve()
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Generate a philosophical response influenced by emotion."""
        prefix = {
            "fear": "S strahom, ",
            "joy": "Z veseljem, ",
            "anger": "Z jezo, ",
        }.get(self.emotion_type, "")

        if self.state == "Ego":
            msg = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            msg = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            msg = "Vse resnice so eno, medsebojno povezane."

        return f"{prefix}{msg} (verzija simbola: {self.symbol.version})"
