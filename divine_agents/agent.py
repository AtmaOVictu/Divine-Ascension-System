class Agent:
    """Ontological agent capable of transitioning states based on emotion and tension."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        # idself represents the agent's identity and guiding principle
        self.idself = {"state": state, "principle": self._principle_for(state)}
        self.iffself = None  # holds last conditional evaluation

    @staticmethod
    def _principle_for(state: str) -> str:
        """Return philosophical principle for a given state."""
        if state == "Ego":
            return "Truth is absolute and independent."
        if state == "Jaz":
            return "Truth is relative and shaped by relations."
        return "All truths are one and interconnected."

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        # heightened emotion increases internal tension
        self.tension += value
        self.evaluate_conditions()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.evaluate_conditions()

    def evaluate_conditions(self) -> dict:
        """Evaluate whether a state transition should occur."""
        decision = "wait"
        if self.tension > 0.7 or self.emotion > 0.5:
            decision = "transition"
        self.iffself = {
            "decision": decision,
            "tension": self.tension,
            "emotion": self.emotion,
        }
        return self.iffself

    def _update_identity(self) -> None:
        """Refresh idself when state changes."""
        self.idself = {"state": self.state, "principle": self._principle_for(self.state)}

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        self.evaluate_conditions()
        if self.iffself["decision"] == "transition":
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            self._update_identity()
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer based on current state and emotion."""
        base = ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            return base + " Čutim to zelo močno."
        if self.emotion < 0.2:
            return base + " O tem razmišljam mirno."
        return base
