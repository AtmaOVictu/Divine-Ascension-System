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


class OracleAgent(Agent):
    """Agent with memory of state transitions and simple prediction capability."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.transitions = []  # list of dictionaries recording from/to states

    def transition(self) -> str:
        """Override to store transition path before switching state."""
        prev_state = self.state
        new_state = super().transition()
        if prev_state != new_state:
            self.transitions.append({"from": prev_state, "to": new_state})
        return new_state

    def suggest_next_step(self, current_state: str) -> list[str]:
        """Return possible next states based on transition history."""
        return [t["to"] for t in self.transitions if t["from"] == current_state]

    def predict_future(self) -> str | None:
        """Predict the most likely next state based on the last transition."""
        if not self.transitions:
            return None
        last = self.transitions[-1]
        return last["to"]
