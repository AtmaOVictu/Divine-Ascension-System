class Agent:
    """Ontological agent capable of emotional state transitions."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"
    STATES = (EGO, JAZ, ENOTNOST)

    PHILOSOPHY = {
        EGO: "Resnica je absolutna in neodvisna od drugih.",
        JAZ: "Resnica je relativna, oblikovana z našimi odnosi.",
        ENOTNOST: "Vse resnice so eno, medsebojno povezane.",
    }

    def __init__(self, name: str, state: str = EGO, tension: float = 0.0,
                 emotion: float = 0.0, emotion_name: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def apply_emotion(self, name: str, intensity: float) -> None:
        """Set emotion and adjust tension accordingly."""
        self.emotion_name = name
        self.emotion = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition when thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == self.EGO:
                self.state = self.JAZ
            elif self.state == self.JAZ:
                self.state = self.ENOTNOST
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by current state."""
        base = self.PHILOSOPHY.get(self.state, "")
        if self.emotion_name != "neutral" and self.emotion > 0.5:
            return f"({self.emotion_name}) {base}"
        return base
