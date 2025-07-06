class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.error_signal = None

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

    # --- Error handling communication ------------------------------------
    def transfer_error(self, target_agent: "Agent") -> None:
        """Transfer information about the current error to ``target_agent``."""
        error_info = (
            self.error_signal
            or f"Error at {self.state}: Tension={self.tension}, Emotion={self.emotion}"
        )
        target_agent.receive_error(error_info)

    def receive_error(self, error_info: str) -> None:
        """Receive an error description and attempt to correct it."""
        self.error_signal = error_info
        self.correct_error()

    def correct_error(self) -> None:
        """Basic correction logic adjusting tension and emotion levels."""
        if self.tension > 0.7:
            self.tension -= 0.1
        if self.emotion > 0.5:
            self.emotion -= 0.1
