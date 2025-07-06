class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, energy: float = 50.0) -> None:
        """Create a new agent with ontological state and energy level."""
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.energy = energy
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_energy(self, value: float) -> None:
        """Adjust energy level."""
        self.energy += value

    def apply_capacitor(self, factor: float) -> None:
        """Modify energy and tension based on a capacitor factor."""
        import random
        self.update_energy(factor * random.uniform(0.8, 1.2))
        self.update_tension(self.tension + factor * random.uniform(0.5, 1.5))

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
