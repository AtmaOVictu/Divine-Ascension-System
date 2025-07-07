class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type or "neutral"
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        if emotion_type:
            self.emotion_type = emotion_type
        self.tension = min(1.0, self.tension + value)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, min(1.0, value))

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
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            if self.emotion_type == "anger":
                return "Resnica je absolutna! Nih\u010de me ne more prepri\u010dati v nasprotno."
            if self.emotion_type == "fear":
                return "Resnica mora biti absolutna, sicer se bojim kaosa."
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            if self.emotion_type == "joy":
                return "Menim, da se resnica rodi v odnosih med nami."
            if self.emotion_type == "sorrow":
                return "V\u010dasih se mi zdi, da je resnica odvisna od tega, koga sre\u010demo."
            return "Resnica je relativna, oblikovana z na\u0161imi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
