class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Emotion and tension values are clamped to the interval ``[0.0, 1.0]`` to
        avoid unrealistic escalation.
        """
        self.emotion = max(0.0, min(1.0, value))
        self.tension = max(0.0, min(1.0, self.tension + self.emotion))

    def update_tension(self, value: float) -> None:
        """Directly set tension level, clamped to ``[0.0, 1.0]``."""
        self.tension = max(0.0, min(1.0, value))

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
        """Return a philosophical answer depending on the current state.

        The *question* influences the response allowing more contextual
        interactions. Only basic keyword matching is used here for brevity.
        """
        text = question.lower()

        if self.state == "Ego":
            if "truth" in text or "resnica" in text:
                return "Resnica je absolutna in neodvisna od drugih."
            return "Verjamem v svojo lastno resnico."

        if self.state == "Jaz":
            if "truth" in text or "resnica" in text:
                return "Resnica je relativna, oblikovana z našimi odnosi."
            return "Resnico gradimo skupaj, preko odnosov." 

        # Enotnost
        if "truth" in text or "resnica" in text:
            return "Vse resnice so eno, medsebojno povezane."
        return "Vidim enotnost v vsem." 
