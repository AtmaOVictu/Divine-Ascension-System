class Agent:
    """Ontological agent capable of emotional reasoning and state transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        # idself defines the agent identity and philosophical principles
        self.idself = {
            "role": state,
            "principles": [
                "Truth is absolute" if state == "Ego" else (
                    "Truth is relative" if state == "Jaz" else "Truth is unified"
                )
            ],
        }
        # iffself will hold conditional decisions derived from emotions
        self.iffself = None
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity, adjust tension and evaluate conditions."""
        self.emotion = value
        self.tension += value
        self.evaluate_conditions()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.evaluate_conditions()

    def evaluate_conditions(self) -> None:
        """Determine iffself based on current emotional state."""
        if self.emotion > 0.8:
            self.iffself = {"decision": "act immediately", "priority": "high"}
        elif self.emotion > 0.5:
            self.iffself = {"decision": "analyze deeply", "priority": "medium"}
        else:
            self.iffself = {"decision": "wait", "priority": "low"}

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
        base = ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            base += f" (občutek: {self.emotion:.2f})"
        return base
