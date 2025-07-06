"""Core definitions for ontological agents."""

from __future__ import annotations



class Agent:
    """Ontological agent capable of philosophical state transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion_level: float = 0.0,
        emotion_type: str = "neutral",
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_level = emotion_level
        self.emotion_type = emotion_type
        self.history = [state]

    # ------------------------------------------------------------------
    # Emotion and tension handling
    # ------------------------------------------------------------------
    def update_emotion(self, emotion_type: str, value: float) -> None:
        """Update emotion level and adjust tension.

        Fear or anger increase tension, while joy can reduce it slightly.
        """

        self.emotion_type = emotion_type
        self.emotion_level = value

        if emotion_type in {"fear", "anger"}:
            self.tension += value
        elif emotion_type == "joy":
            self.tension = max(0.0, self.tension - value / 2)
        else:
            self.tension += value / 2

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        prefix = {
            "fear": "Z zaskrbljenostjo pravim:",
            "anger": "Z jezo trdim:",
            "joy": "Z veseljem povem:",
        }.get(self.emotion_type, "Pravim:")

        if self.state == "Ego":
            message = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            message = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            message = "Vse resnice so eno, medsebojno povezane."

        return f"{prefix} {message}"
