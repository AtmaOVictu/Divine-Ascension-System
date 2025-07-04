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
        self.steps = []  # store optimization info for each created step

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
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} (Čustveni nivo: {self.emotion:.2f})"

    # --- step and optimization functionality ---
    def create_step(self) -> None:
        """Create a new step and store its binary optimization."""
        self.step_count += 1
        binary = bin(self.step_count)[2:]
        self.steps.append({"step": self.step_count, "binary": binary})

    def seciraj(self) -> None:
        """Simulate continuous exploration by creating a new optimized step."""
        self.history.append("SECIRAJ")
        self.create_step()

    def progress_table(self):
        """Return the table of created steps."""
        return list(self.steps)
