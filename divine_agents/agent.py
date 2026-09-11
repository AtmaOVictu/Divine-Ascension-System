class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.frames = [
            {
                "state": self.state,
                "emotion": self.emotion,
                "tension": self.tension,
            }
        ]

    def _record_frame(self) -> None:
        """Record the current state, emotion, and tension as a frame."""
        self.frames.append(
            {
                "state": self.state,
                "emotion": self.emotion,
                "tension": self.tension,
            }
        )

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
        self._record_frame()
        return self.state

    def get_frames(self) -> list:
        """Return the recorded frames of the agent's evolution."""
        return self.frames

    def get_history(self) -> list:
        """Return the history of state transitions."""
        return self.history

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            return f"{base} Čustva močno vplivajo na moj odgovor."
        return base
