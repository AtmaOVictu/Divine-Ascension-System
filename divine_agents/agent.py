class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = ""
        self.history = [state]
        self.commitment = None

    def update_emotion(self, value: float, label: str = "") -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        if label:
            self.emotion_label = label
        self.tension += value
        self.evaluate_commitment()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.evaluate_commitment()

    def make_commitment(self, commitment: str) -> None:
        """Set the agent's commitment."""
        self.commitment = commitment
        self.history.append(f"{self.name} has committed to {commitment}.")

    def evaluate_commitment(self) -> None:
        """Update state based on current commitment and emotion label."""
        if self.commitment == "self-preservation" and self.emotion_label == "anger":
            self.state = "High Tension"
            self.history.append(
                f"{self.name} is in High Tension due to commitment to self-preservation."
            )
        elif self.commitment == "self-awareness" and self.emotion_label == "reflection":
            self.state = "Jaz"
            self.history.append(
                f"{self.name} is in Jaz due to commitment to self-awareness."
            )
        elif self.commitment is not None:
            self.state = "Neutral"
            self.history.append(f"{self.name} is in Neutral state.")

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
