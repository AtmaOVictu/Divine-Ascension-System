class Agent:
    """Represents an ontological agent capable of transitioning states and
    responding philosophically based on emotion and tension."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def speak(self, question: str) -> str:
        """Return an answer colored by the agent's emotional intensity."""
        base = self.respond(question)
        if self.emotion > 0.5:
            tone = "s strastjo"
        elif self.emotion < -0.5:
            tone = "z zaskrbljenostjo"
        else:
            tone = "mirno"
        return f"{self.name} {tone} odgovarja: {base}"

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

    @property
    def philosophical_principle(self) -> str:
        """Return the core principle associated with the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        return self.philosophical_principle
