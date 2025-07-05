class Agent:
    """Ontological agent able to transition between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTION_THRESHOLD = 0.5
    TENSION_THRESHOLD = 0.7

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, delta: float) -> None:
        """Increase emotion intensity and adjust tension accordingly."""
        self.emotion += delta
        self.tension += delta

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > self.TENSION_THRESHOLD or self.emotion > self.EMOTION_THRESHOLD:
            current_index = self.STATES.index(self.state)
            if current_index < len(self.STATES) - 1:
                self.state = self.STATES[current_index + 1]
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.7:
            return base.upper()
        if self.emotion > 0.3:
            return f"{base} (čustveno)"
        return base
