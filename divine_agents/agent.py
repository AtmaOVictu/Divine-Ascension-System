from .utils import logistic_function


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        k: float = 10.0,
        c: float = 0.5,
    ):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.k = k
        self.c = c
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.evolve()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.evolve()

    def evolve(self) -> None:
        """Update tension using a logistic curve."""
        self.tension = logistic_function(self.tension, self.k, self.c)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        effective_tension = logistic_function(self.tension, self.k, self.c)
        if effective_tension > 0.7 or self.emotion > 0.5:
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
        return f"{base} (čustvo: {self.emotion:.2f})"
