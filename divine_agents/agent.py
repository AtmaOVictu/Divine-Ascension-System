class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        # store frames of state, emotion and tension for later analysis
        self.frames = [{"state": state, "emotion": emotion, "tension": tension}]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
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
        self.frames.append({"state": self.state, "emotion": self.emotion, "tension": self.tension})
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        emotional_prefix = ""
        if self.emotion >= 0.7:
            emotional_prefix = "Z ognjevitostjo, "
        elif self.emotion >= 0.3:
            emotional_prefix = "S čustvi, "

        if self.state == "Ego":
            core = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            core = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            core = "Vse resnice so eno, medsebojno povezane."

        return f"{emotional_prefix}{core}"

    def get_frames(self):
        """Return the historical frames describing the agent's evolution."""
        return self.frames
