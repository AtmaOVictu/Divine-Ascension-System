from __future__ import annotations

from typing import Dict


class Agent:
    """Ontological agent capable of state transitions and emotional responses."""

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
        self.emotions: Dict[str, float] = emotions or {}
        self.history = [state]

    # ------------------------------------------------------------------
    # Emotional updates and state management
    # ------------------------------------------------------------------
    def update_emotion(self, emotion_type: str, value: float) -> None:
        """Update a specific emotion and adjust tension if necessary."""

        self.emotions[emotion_type] = value
        if emotion_type in {"fear", "anger"}:
            self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""

        self.tension = value

    def _emotion_intensity(self) -> float:
        """Return the strongest emotion intensity."""

        return max(self.emotions.values(), default=0.0)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""

        if self.tension > 0.7 or self._emotion_intensity() > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    # ------------------------------------------------------------------
    # Dialogue helpers
    # ------------------------------------------------------------------
    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on state and emotions."""

        if self.state == "Ego":
            truth = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            truth = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            truth = "Vse resnice so eno, medsebojno povezane."

        emotion_phrase = ""
        if self.emotions.get("fear", 0) > 0.5:
            emotion_phrase = " Občutim strah."
        elif self.emotions.get("joy", 0) > 0.5:
            emotion_phrase = " Preveva me veselje."
        elif self.emotions.get("anger", 0) > 0.5:
            emotion_phrase = " Čutim jezo."

        return f"{truth}{emotion_phrase}"
