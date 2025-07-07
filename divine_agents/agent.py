class Agent:
    """Ontological agent capable of emotional reasoning and state transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

        # idself defines the agent's philosophical identity
        self.idself = {
            "role": "Philosopher",
            "principles": ["logic", "emotion", "growth"],
        }

        # iffself stores the decision context based on current emotion
        self.iffself = self.evaluate_conditions()

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.iffself = self.evaluate_conditions()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.iffself = self.evaluate_conditions()

    def evaluate_conditions(self) -> dict:
        """Determine action decision based on current emotion level."""
        if self.emotion > 0.5:
            return {"decision": "act", "priority": "high"}
        elif self.emotion < -0.5:
            return {"decision": "withdraw", "priority": "low"}
        return {"decision": "contemplate", "priority": "medium"}

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

        if self.emotion > 0.5:
            base += " Čustveno me to gane."
        return base
