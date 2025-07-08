import random
from .capacitor import InvalidCapacitor


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.capacitor = InvalidCapacitor()

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.capacitor.validate_operation(f"update_emotion({value})", self.state)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.capacitor.validate_operation(f"update_tension({value})", self.state)

    def apply_shadow(self) -> None:
        """Apply opposing emotional forces reducing tension and emotion."""
        shadow = random.uniform(0.1, 0.3)
        self.update_tension(max(0.0, self.tension - shadow))
        self.update_emotion(max(0.0, self.emotion - shadow))
        self.history.append(f"shadow:{shadow:.2f}")
        self.capacitor.validate_operation("apply_shadow", self.state)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        self.capacitor.validate_operation(f"transition->{self.state}", self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
