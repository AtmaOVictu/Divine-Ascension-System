class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 loyalty: float = 0.5, experiences=None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.loyalty = loyalty
        self.experiences = experiences or []
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def add_experience(self, text: str) -> None:
        """Record an experience influencing future transitions."""
        self.experiences.append(text)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        emotion_val = self.emotion if isinstance(self.emotion, (int, float)) else 1.0
        if self.tension > 0.7 or emotion_val > 0.5:
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

        emotion_val = self.emotion if isinstance(self.emotion, (int, float)) else 1.0
        if emotion_val > 0.5:
            return f"Moja custva vplivajo name, vendar verjamem, da {base}"
        return base
