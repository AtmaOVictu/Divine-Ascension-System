class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent holds an ontological ``state`` (``Ego``, ``Jaz`` or ``Enotnost``),
    an ``emotion`` intensity and a ``tension`` level.  Tension is influenced by
    emotions and both values determine when a state transition occurs.
    """

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

    #
    def emotion_descriptor(self) -> str:
        """Return a human readable description of the current emotion level."""
        if self.emotion > 0.6:
            return "vznemirjeno"
        if self.emotion > 0.3:
            return "nezadovoljno"
        return "mirno"

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
        """Return a philosophical answer influenced by state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} (odziv {self.emotion_descriptor()})"

    def speak(self, question: str) -> str:
        """Generate a dialogue line and attempt a state transition."""
        line = f"{self.name} ({self.state}): {self.respond(question)}"
        self.transition()
        return line
