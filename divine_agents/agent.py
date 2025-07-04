class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0, emotion: float = 0.0, emotion_label: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    def update_emotion(self, label: str, intensity: float) -> None:
        """Update emotion and adjust tension accordingly."""
        self.emotion_label = label
        self.emotion = intensity
        self.tension += intensity

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
        """Return a philosophical answer depending on state and emotion."""
        base = ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_label == "fear":
            return f"(Boječe) {base}"
        if self.emotion_label == "joy":
            return f"(Veselo) {base}"
        if self.emotion_label == "anger":
            return f"(Jezo) {base}"
        return base

    def speak(self, question: str) -> str:
        """Produce a line of dialogue reflecting the agent's state."""
        answer = self.respond(question)
        return f"{self.name} ({self.state}): {answer}"

    def transition_line(self) -> str:
        """Transition state if needed and return a log line."""
        new_state = self.transition()
        return f"{self.name} prehaja v stanje: {new_state}"
