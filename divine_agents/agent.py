class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, feeling: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.feeling = feeling or "neutral"
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def apply_emotion_effect(self, feeling: str) -> None:
        """Modify tension and emotion based on the given feeling."""
        self.feeling = feeling
        modifiers = {
            "fear": 0.3,
            "anger": 0.4,
            "joy": -0.2,
            "neutral": 0.0,
        }
        delta = modifiers.get(feeling, 0.0)
        self.tension += delta
        self.emotion = max(0.0, min(1.0, self.emotion + delta))

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
        """Return a philosophical answer influenced by state and feeling."""
        prefix = {
            "fear": "(prestrašeno) ",
            "anger": "(jezno) ",
            "joy": "(radostno) ",
            "neutral": "",
        }.get(self.feeling, "")

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return prefix + base
