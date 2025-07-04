class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    #: Mapping of emotion labels to intensity values.
    EMOTION_LEVELS = {
        "fear": 0.8,
        "anger": 0.7,
        "joy": 0.6,
        "sorrow": 0.5,
        "doubt": 0.6,
        "neutral": 0.0,
    }

    #: Philosophical response per ontological state.
    PHILOSOPHY = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, emotion: str) -> None:
        """Update emotion intensity based on an emotion label."""
        value = self.EMOTION_LEVELS.get(emotion, 0.0)
        self.emotion = value
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
        return self.PHILOSOPHY.get(self.state, "")

    def speak(self) -> str:
        """Return the agent's current philosophical position."""
        return self.respond("Kaj je resnica?")
