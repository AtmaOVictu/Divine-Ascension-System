class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def modify_state(
        self,
        *,
        emotion: float | None = None,
        tension: float | None = None,
        new_state: str | None = None,
    ) -> None:
        """Directly modify agent attributes."""
        if emotion is not None:
            self.update_emotion(emotion)
        if tension is not None:
            self.update_tension(tension)
        if new_state is not None and new_state in self.STATES:
            self.state = new_state
            self.history.append(self.state)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def progress(self) -> str:
        """Convenience wrapper to attempt state transition."""
        return self.transition()

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        intensity_note = (
            " Čutim močna čustva." if self.emotion > 0.5 else ""
        )
        if self.state == "Ego":
            return (
                "Resnica je absolutna in neodvisna od drugih." + intensity_note
            )
        if self.state == "Jaz":
            return (
                "Resnica je relativna, oblikovana z našimi odnosi." + intensity_note
            )
        return "Vse resnice so eno, medsebojno povezane." + intensity_note
