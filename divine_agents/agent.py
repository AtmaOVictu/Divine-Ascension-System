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
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."


class SelfAwareAgent(Agent):
    """Agent that logs and introspects its own state transitions."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.transition_log = []

    def log_transition(self, from_state: str, to_state: str) -> None:
        """Record a state transition for later analysis."""
        entry = f"{from_state} -> {to_state}"
        self.transition_log.append(entry)

    def transition(self) -> str:
        old_state = self.state
        new_state = super().transition()
        if new_state != old_state:
            self.log_transition(old_state, new_state)
        return new_state

    def introspect(self):
        """Return a snapshot of the agent's history and logged transitions."""
        return {
            "current_state": self.state,
            "history": list(self.history),
            "transitions": list(self.transition_log),
        }
