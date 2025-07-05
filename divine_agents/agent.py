class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    TRANSITION_TENSION = 0.7
    TRANSITION_EMOTION = 0.5

    MAX_TENSION = 1.0
    MAX_EMOTION = 1.0
    MAX_INTERACTION = 1.0
    MAX_EXTERNAL = 1.0

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.last_error = 0.0

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def evaluate_transition(self, interaction: float = 0.0, external: float = 0.0, alpha: float = 1.0) -> tuple[bool, float]:
        """Return whether transition factors exceed alpha and compute error."""
        factor_sum = (
            self.tension / self.MAX_TENSION
            + self.emotion / self.MAX_EMOTION
            + interaction / self.MAX_INTERACTION
            + external / self.MAX_EXTERNAL
        )
        error = abs(factor_sum - alpha)
        self.last_error = error
        return factor_sum > alpha, error

    def transition(self, interaction: float = 0.0, external: float = 0.0) -> str:
        """Perform state transition when thresholds are exceeded."""
        self.evaluate_transition(interaction, external)
        if self.tension > self.TRANSITION_TENSION or self.emotion > self.TRANSITION_EMOTION:
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

        if self.emotion > self.TRANSITION_EMOTION:
            base += " Čutim močna čustva, ki barvajo moje razumevanje."
        return base
