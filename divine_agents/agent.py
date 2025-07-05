class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def calculate_tension(self) -> float:
        """Return tension as a dynamic force based on emotion."""
        return (self.emotion ** 2) / (1 + self.tension)

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and recalculate tension."""
        self.emotion = value
        self.tension = self.calculate_tension()

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

    def emotional_respond(self, question: str) -> str:
        """Return a response influenced by the agent's emotion."""
        base = self.respond(question)
        if self.emotion > 0.7:
            prefix = "S strastjo odgovarjam: "
        elif self.emotion > 0.3:
            prefix = "Mirno pojasnim: "
        else:
            prefix = "Brez čustev povem: "
        return prefix + base
