class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.step_count = 0
        self.optimized_steps = []

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

    # Optimization and progression utilities
    def seciraj(self) -> str:
        """Create a new step and apply binary optimization."""
        self.create_new_step()
        binary = self.optimized_steps[-1]
        return f"Step {self.step_count} created (binary {binary})"

    def create_new_step(self) -> None:
        """Increment the internal step counter and store binary optimization."""
        self.step_count += 1
        self.history.append(f"Step {self.step_count}")
        self.apply_binary_optimization()

    def apply_binary_optimization(self) -> None:
        """Convert the current step count to binary for optimized tracking."""
        binary = self.convert_to_binary(self.step_count)
        self.optimized_steps.append(binary)

    @staticmethod
    def convert_to_binary(number: int) -> str:
        """Return the binary representation of a number without prefix."""
        return bin(number)[2:]
