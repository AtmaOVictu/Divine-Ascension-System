class Agent:
    """Represent an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity, type and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        if emotion_type is not None:
            self.emotion_type = emotion_type

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
        """Return a philosophical answer influenced by the current emotion."""
        emotion_note = (
            f"Ob občutku {self.emotion_type}, " if self.emotion_type else ""
        )
        if self.state == "Ego":
            return emotion_note + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return emotion_note + "Resnica je relativna, oblikovana z našimi odnosi."
        return emotion_note + "Vse resnice so eno, medsebojno povezane."
