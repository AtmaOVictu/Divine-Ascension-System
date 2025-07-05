"""Core agent logic for ontological state transitions and responses."""


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        unity_progress: float = 0.01,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.unity_progress = unity_progress
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

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by current state and emotion."""
        base = ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            base += " Čutim močna čustva ob tem."  # emotional emphasis
        return base

    def update_unity(self, increment: float = 0.01) -> float:
        """Update unity progress from 0.01 to 1.00 as a cyclical loading screen."""
        self.unity_progress += increment
        if self.unity_progress > 1.00:
            self.unity_progress = 0.01
        elif self.unity_progress < 0.01:
            self.unity_progress = 1.00
        return self.unity_progress
