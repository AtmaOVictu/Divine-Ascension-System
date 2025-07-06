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

    # --- error handling and communication ---

    def transfer_error(self, target_agent: "Agent") -> None:
        """Transfer this agent's error state to another agent for correction."""
        self.error_signal = (
            f"Error at {self.state}: Tension={self.tension}, Emotion={self.emotion}"
        )
        target_agent.receive_error(self.error_signal, self)

    def receive_error(self, error_info: str, source_agent: "Agent") -> None:
        """Receive an error signal from another agent and attempt correction."""
        self.error_signal = error_info
        self.correct_error(source_agent)

    def correct_error(self, agent: "Agent") -> None:
        """Reduce tension and emotion on the provided agent."""
        if agent.tension > 0.7:
            agent.tension -= 0.1
        if agent.emotion > 0.5:
            agent.emotion -= 0.1
