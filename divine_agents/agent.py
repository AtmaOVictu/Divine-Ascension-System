class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    MEGA_THRESHOLD = 1.0

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.nano_count = 0
        self.history = [state]

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
        return self.state

    def nano_event(self, delta_tension: float = 0.1, delta_emotion: float = 0.1) -> str:
        """Apply a micro change that may trigger a standard transition."""
        self.nano_count += 1
        self.tension += delta_tension
        self.emotion += delta_emotion
        return self.transition()

    def mega_transition(self) -> str:
        """Perform a larger jump directly to 'Enotnost' if thresholds are high."""
        if self.tension > self.MEGA_THRESHOLD or self.emotion > 0.8:
            self.state = "Enotnost"
        else:
            self.transition()
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
