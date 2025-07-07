from .thresholds import SymbolicBox


class Agent:
    """Ontological agent capable of state transitions based on tension and emotion."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.box = SymbolicBox(stage=state, data={"agent": name})
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    # expose state via property so external code can access current stage
    @property
    def state(self) -> str:
        return self.box.stage

    @state.setter
    def state(self, value: str) -> None:
        self.box.stage = value

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition when thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            next_state = None
            if self.state == "Ego":
                next_state = "Jaz"
            elif self.state == "Jaz":
                next_state = "Enotnost"
            if next_state and self.box.is_valid_transition(next_state):
                self.box.transition(next_state, {"trigger": "threshold"})
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
