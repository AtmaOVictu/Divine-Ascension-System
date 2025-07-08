class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, commitment: str | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.commitment = commitment
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.evaluate_commitment()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.evaluate_commitment()

    def evaluate_commitment(self) -> None:
        """Adjust the state based on commitment and emotional intensity."""
        if not self.commitment:
            return
        prev_state = self.state
        if self.commitment == "self-preservation" and self.emotion > 0.5:
            self.state = "Ego"
        elif self.commitment == "self-awareness" and self.emotion > 0.5:
            self.state = "Jaz"
        elif self.commitment == "unity" and self.emotion > 0.5:
            self.state = "Enotnost"
        if self.state != prev_state:
            self.history.append(self.state)

    def make_commitment(self, commitment: str) -> None:
        """Set the agent's commitment."""
        self.commitment = commitment
        self.history.append(f"commitment:{commitment}")

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
