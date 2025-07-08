class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion_level: float = 0.0, emotion: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_level = emotion_level
        self.emotion = emotion
        self.commitment = None
        self.history = [state]

    def update_emotion(self, value: float, label: str = "neutral") -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion_level = value
        self.emotion = label
        self.tension += value
        self.evaluate_commitment()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.evaluate_commitment()

    def make_commitment(self, commitment: str) -> None:
        """Set a commitment influencing future emotional behavior."""
        self.commitment = commitment
        self.history.append(f"Committed to {commitment}")

    def evaluate_commitment(self) -> None:
        """Adjust tension according to commitment and current emotion."""
        if self.commitment == "self-preservation" and self.emotion == "anger":
            self.tension = min(1.0, self.tension + 0.3)
        elif self.commitment == "self-awareness" and self.emotion in {"reflection", "thoughtful"}:
            self.tension = max(0.0, self.tension - 0.3)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion in {"fear", "anger"}:
            return f"{base} Čutim {self.emotion}."
        if self.emotion == "joy":
            return f"{base} To me navdaja z veseljem."
        return base
