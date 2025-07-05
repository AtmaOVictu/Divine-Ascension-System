class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
    ):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Set emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def feel(self, mood: str) -> None:
        """Modify emotion and tension based on a named feeling."""
        adjustments = {
            "fear": 0.8,
            "anger": 0.7,
            "joy": 0.3,
        }
        delta = adjustments.get(mood, 0.0)
        self.update_emotion(self.emotion + delta)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def intensity(self) -> float:
        """Return current intensity based on tension and emotion."""
        return self.tension * self.emotion

    def transition(self) -> str:
        """Perform state transition if emotion or tension exceeds thresholds."""
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
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.7:
            base += " Moja čustva so zelo močna."
        elif self.emotion > 0.3:
            base += " Čutim rahlo napetost."

        return base
