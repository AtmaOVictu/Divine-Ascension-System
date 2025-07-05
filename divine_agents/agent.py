from .time_tracking import TimeTracker


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.tracker = TimeTracker(self.STATES)
        self.tracker.start(state)

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        new_state = self.state
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                new_state = "Jaz"
            elif self.state == "Jaz":
                new_state = "Enotnost"
        self.tracker.switch(new_state)
        self.state = new_state
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def time_spent(self) -> dict:
        """Return a snapshot of time spent in states."""
        return self.tracker.time_spent
