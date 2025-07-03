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


class NegationAgent(Agent):
    """Agent that emphasizes negation when performing actions."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, negation_factor: int = 1):
        super().__init__(name, state, tension, emotion)
        self.negation_factor = max(1, negation_factor)

    def apply_negation(self, action: str) -> str:
        """Apply negation repeatedly based on ``negation_factor``."""
        result = action
        for _ in range(self.negation_factor):
            result = f"\u00ac({result})"
        return result

    def perform_action(self, action: str) -> str:
        """Record a negated action in the agent's history."""
        negated = self.apply_negation(action)
        self.history.append(negated)
        return negated

    def evolve(self) -> str:
        """Transition state and strengthen negation when active."""
        previous = self.state
        new_state = self.transition()
        if previous != new_state and new_state != "Ego":
            self.negation_factor += 1
        return new_state
