class Agent:
    """Represent an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotions=None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions = emotions if emotions is not None else {
            "fear": 0.0,
            "joy": 0.0,
            "anger": 0.0,
        }
        self.history = [state]

    @property
    def emotion_intensity(self) -> float:
        """Return the highest emotion intensity."""
        return max(self.emotions.values()) if self.emotions else 0.0

    def update_emotion(self, emotion: str, value: float) -> None:
        """Update a specific emotion and adjust tension accordingly."""
        if emotion not in self.emotions:
            raise ValueError(f"Unknown emotion: {emotion}")
        self.emotions[emotion] = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state and emotions."""
        if self.state == "Ego":
            if self.emotions.get("anger", 0.0) > 0.5:
                return "Moja resnica je edina prava!"
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            if self.emotions.get("fear", 0.0) > 0.5:
                return "Morda je resnica odvisna od vseh nas."
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
