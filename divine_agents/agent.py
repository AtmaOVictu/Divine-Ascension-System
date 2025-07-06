class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        loyalty: float = 0.5,
    ):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.loyalty = loyalty
        self.history = [state]
        self.decision_history = []

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

    def make_moral_decision(self, situation: str) -> str:
        """Make a decision influenced by emotion, tension and loyalty."""
        decision = ""
        if self.emotion < 0.3 and self.tension < 0.3:
            decision = f"{self.name} izbere samozaščito v {situation}."
        elif self.state == "Enotnost" or self.loyalty > 0.7:
            decision = f"{self.name} pomaga drugim v {situation}."
        elif self.state == "Jaz":
            decision = f"{self.name} uravnoteži lastne in skupne potrebe v {situation}."
        else:
            decision = f"{self.name} daje prednost sebi v {situation}."

        self.decision_history.append(decision)
        return decision
