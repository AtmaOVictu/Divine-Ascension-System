class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        # Belief statement reflecting the agent's understanding of truth
        self.belief = self._default_belief()

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.update_beliefs()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.update_beliefs()

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

    def speak(self, question: str) -> str:
        """Public method used by dialogue managers."""
        return self.respond(question)

    # ------------------------------------------------------------------
    # Belief management
    # ------------------------------------------------------------------
    def _default_belief(self) -> str:
        """Return the default belief statement for the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def update_beliefs(self) -> None:
        """Adjust beliefs based on current emotion and tension."""
        if self.emotion > 0.5:
            self.belief = "Moja čustva oblikujejo mojo resničnost."
        elif self.tension > 0.7:
            self.belief = "Napetost me vodi k iskanju globlje resnice."
        else:
            self.belief = self._default_belief()
