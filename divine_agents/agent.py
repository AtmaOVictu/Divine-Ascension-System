class Agent:
    """Represent an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_type: str | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, kind: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            New intensity of the emotion between 0 and 1.
        kind:
            Optional name of the emotion (e.g. ``"fear"``, ``"joy"``).
        """

        self.emotion = value
        if kind:
            self.emotion_type = kind
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition when thresholds are exceeded.

        The agent moves from ``Ego`` to ``Jaz`` or ``Jaz`` to ``Enotnost`` when
        ``tension`` is greater than ``0.7`` or ``emotion`` is greater than
        ``0.5``.
        """
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def _emotion_phrase(self) -> str:
        """Return a short phrase describing the agent's current emotion."""
        if not self.emotion_type or self.emotion <= 0.5:
            return ""

        phrases = {
            "fear": "Čutim strah.",
            "anger": "Preveva me jeza.",
            "joy": "Preveva me radost.",
            "sorrow": "Občutim žalost.",
        }
        return phrases.get(self.emotion_type, "")

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        emotion_text = self._emotion_phrase()
        return f"{base} {emotion_text}".strip()
