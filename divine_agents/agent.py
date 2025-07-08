from .time_manager import TimeManager


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 *, time_manager: TimeManager | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.will = 0.0
        self.faith = 0.0
        self.history = [state]
        self.time_manager = time_manager if time_manager else TimeManager()

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = max(0.0, min(1.0, value))
        self.tension = max(0.0, min(1.0, self.tension + value))
        self.faith = self.emotion * 0.7
        self.time_manager.update_time(self)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, min(1.0, value))
        self.will = self.tension * 0.8
        self.time_manager.update_time(self)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        self.time_manager.update_time(self)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def report(self) -> dict:
        """Return a summary of the agent and time status."""
        return {
            "name": self.name,
            "state": self.state,
            "tension": self.tension,
            "emotion": self.emotion,
            "will": self.will,
            "faith": self.faith,
            "history": list(self.history),
            "time": self.time_manager.report(),
        }
