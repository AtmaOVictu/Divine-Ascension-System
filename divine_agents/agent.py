class Agent:
    """Ontological agent capable of state transitions and emotional responses."""

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

    def update_emotion(self, value: float, emotion_type: str) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.emotion_type = emotion_type
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

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by emotion and state."""
        prefix_map = {
            "fear": "V strahu verjamem, da",
            "joy": "Z veseljem trdim, da",
            "anger": "V jezi verjamem, da",
        }

        prefix = "" if not self.emotion_type else f"{prefix_map.get(self.emotion_type, 'Čutim, da')}"

        if self.state == "Ego":
            base = "resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "vse resnice so eno, medsebojno povezane."

        if prefix:
            return f"{prefix} {base}"
        return base.capitalize()
