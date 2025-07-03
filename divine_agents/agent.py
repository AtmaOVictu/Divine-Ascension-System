"""Ontological agent model with emotional state and transitions."""

class Agent:
    """Represent an agent capable of ontological state transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        """Initialize an agent with a name, starting state and emotion."""
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

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

    # Utility methods -----------------------------------------------------
    def emotion_label(self) -> str:
        """Return a human readable label for the current emotion."""
        if self.emotion > 0.7:
            return "jeza"
        if self.emotion > 0.5:
            return "strah"
        if self.emotion < 0.2:
            return "mir"
        return "nevtralno"

    def speak(self, question: str) -> str:
        """Generate a dialogue line based on state and emotion."""
        base = self.respond(question)
        return f"{base} (čustvo: {self.emotion_label()})"
