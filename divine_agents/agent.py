class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_name: str = ""):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, value: float, name: str = "") -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value: float
            New emotional intensity between 0 and 1.
        name: str, optional
            Descriptive name of the emotion (e.g. fear, joy).
        """
        self.emotion = value
        self.emotion_name = name
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
        """Return a philosophical answer depending on the current state."""
        emotion_note = f" Čutim {self.emotion_name}." if self.emotion_name else ""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih." + emotion_note
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi." + emotion_note
        return "Vse resnice so eno, medsebojno povezane." + emotion_note
