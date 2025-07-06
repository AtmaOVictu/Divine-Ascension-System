class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotions: dict | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions = {"fear": 0.0, "joy": 0.0, "anger": 0.0}
        if emotions:
            self.emotions.update(emotions)
        self.history = [state]

    def set_emotion(self, emotion: str, value: float) -> None:
        """Set an emotion level and adjust tension accordingly."""
        if emotion in self.emotions:
            self.emotions[emotion] = value
            self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        emotion_threshold = max(self.emotions.values())
        if self.tension > 0.7 or emotion_threshold > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state and emotions."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotions.get("anger", 0) > 0.5:
            return f"(jezen) {base}"
        if self.emotions.get("fear", 0) > 0.5:
            return f"(prestrašen) {base}"
        if self.emotions.get("joy", 0) > 0.5:
            return f"(vesel) {base}"
        return base
