from .log import Log
from .flow import Flow


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, *, log: Log | None = None, flow: Flow | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.log = log if log else Log()
        self.flow = flow if flow else Flow("main", initial_state=state)

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.log.add(f"{self.name} emotion updated to {self.emotion}")

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.log.add(f"{self.name} tension set to {self.tension}")

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            old_state = self.state
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            if old_state != self.state:
                self.log.add(f"{self.name} transitioned from {old_state} to {self.state}")
                self.flow.update(self.state)
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            answer = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            answer = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            answer = "Vse resnice so eno, medsebojno povezane."
        reply = f"{answer} Emotion: {self.emotion:.2f}"
        self.log.add(f"{self.name} responded: {reply}")
        return reply
