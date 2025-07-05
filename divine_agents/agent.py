import math


def logistic_function(t: float, k: float = 1.0, c: float = 0.5) -> float:
    """Simple logistic function used to smooth state transitions."""
    return 1 / (1 + math.exp(-k * (t - c)))


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    THRESHOLD_TENSION = 0.7
    THRESHOLD_EMOTION = 0.5

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.k = 1.0  # logistic curve steepness
        self.c = 0.5  # logistic curve midpoint

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def evolve(self) -> None:
        """Update tension using a logistic function based on current emotion."""
        self.tension = logistic_function(self.tension + self.emotion, self.k, self.c)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        self.evolve()
        if self.tension > self.THRESHOLD_TENSION or self.emotion > self.THRESHOLD_EMOTION:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            truth = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            truth = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            truth = "Vse resnice so eno, medsebojno povezane."

        tone = "mirno" if self.emotion <= 0.5 else "strastno"
        return f"{tone.capitalize()} odgovarjam: {truth}"
