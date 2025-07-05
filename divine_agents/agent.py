class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters are clamped between 0 and 1 to keep emotion and tension in
    reasonable bounds.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "calm") -> None:
        self.name = name
        self.state = state
        self.tension = max(0.0, min(tension, 1.0))
        self.emotion = max(0.0, min(emotion, 1.0))
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = max(0.0, min(value, 1.0))
        if emotion_type:
            self.emotion_type = emotion_type
        self.tension = max(0.0, min(self.tension + self.emotion, 1.0))

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, min(value, 1.0))

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
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        if self.emotion_type != "calm":
            base += f" Čutim {self.emotion_type}."
        return base
