from .emotions import Emotions


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotions: Emotions | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions = emotions or Emotions()
        self.history = [state]

    def update_emotions(self, **kwargs) -> None:
        """Update emotion values and adjust tension accordingly."""
        for key, value in kwargs.items():
            if hasattr(self.emotions, key):
                setattr(self.emotions, key, value)
        self._adjust_tension_from_emotions()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def _adjust_tension_from_emotions(self) -> None:
        """Modify tension based on emotional state."""
        self.tension += (self.emotions.fear + self.emotions.anger) * 0.5
        self.tension -= self.emotions.joy * 0.3
        self.tension = max(0.0, min(1.5, self.tension))

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotions.intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str | None = None) -> str:
        """Return a philosophical answer depending on the current state and emotions."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotions.anger > 0.5:
            return f"Z jezo trdim: {base}"
        if self.emotions.joy > 0.5:
            return f"Z veseljem povem: {base}"
        if self.emotions.fear > 0.5:
            return f"S strahom priznavam: {base}"
        return base
