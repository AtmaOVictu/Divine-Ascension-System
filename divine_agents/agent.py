from .logs import Log, Flow


class Agent:
    """Ontological agent capable of state transitions with logging."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        log: Log | None = None,
        flow: Flow | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.log = log if log is not None else Log()
        self.flow = flow if flow is not None else Flow(f"{self.name}_flow", state)
        self.log.add_entry(f"{self.name} initialized in state {self.state}")

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.log.add_entry(
            f"{self.name} emotion updated to {self.emotion} (tension={self.tension})"
        )

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.log.add_entry(f"{self.name} tension set to {self.tension}")

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        self.log.add_entry(f"{self.name} transitioned to {self.state}")
        self.flow.update_state(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            reply = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            reply = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            reply = "Vse resnice so eno, medsebojno povezane."
        self.log.add_entry(f"{self.name} responded: {reply}")
        return reply
