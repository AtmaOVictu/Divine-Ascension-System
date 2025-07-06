class Agent:
    """Represent an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion_type: str = "neutral", emotion_level: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_type = emotion_type
        self.emotion_level = emotion_level
        self.history = [state]

    def update_emotion(self, emotion_type: str, intensity: float) -> None:
        """Update emotion and adjust tension accordingly."""
        self.emotion_type = emotion_type
        self.emotion_level = intensity
        if emotion_type in {"fear", "anger"}:
            self.tension += intensity
        else:
            self.tension += intensity * 0.5

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
        base: str
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} (Čustvo: {self.emotion_type})"
