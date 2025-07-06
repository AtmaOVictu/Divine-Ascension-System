class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotions: dict | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        if emotions is None:
            emotions = {"fear": 0.0, "joy": 0.0, "anger": 0.0}
        self.emotions = emotions
        self.history = [state]

    def update_emotion(self, emotion: str, value: float) -> None:
        """Update a specific emotion and adjust tension accordingly."""
        if emotion not in self.emotions:
            raise ValueError("Unknown emotion")
        self.emotions[emotion] = value
        self.tension += value

    def emotion_level(self) -> float:
        """Return the highest intensity among emotions."""
        return max(self.emotions.values())

    def dominant_emotion(self) -> str:
        """Return the emotion with the highest intensity."""
        return max(self.emotions, key=self.emotions.get)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level() > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer based on current state and emotion."""
        prefix_map = {
            "fear": "V strahu izjavljam: ",
            "anger": "Z jezo trdim: ",
            "joy": "Z veseljem povem: ",
        }
        prefix = prefix_map.get(self.dominant_emotion(), "")

        if self.state == "Ego":
            message = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            message = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            message = "Vse resnice so eno, medsebojno povezane."
        return f"{prefix}{message}"
