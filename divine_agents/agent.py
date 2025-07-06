class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    #: Mapping of simple emotion labels to intensity values.  These
    #: intensities are also added to ``tension`` when emotions change.
    EMOTION_VALUES = {
        "neutral": 0.0,
        "joy": 0.6,
        "fear": 0.8,
        "anger": 0.7,
        "sorrow": 0.5,
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = "neutral"
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def set_emotion(self, label: str) -> None:
        """Set emotion by label and update tension accordingly."""
        if label not in self.EMOTION_VALUES:
            raise ValueError(f"Unknown emotion: {label}")
        self.emotion_label = label
        self.update_emotion(self.EMOTION_VALUES[label])

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
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def speak_truth(self) -> str:
        """Return the agent's view of truth including emotion label."""
        statement = self.respond("Kaj je resnica?")
        if self.emotion_label != "neutral":
            return f"{self.emotion_label.capitalize()} povem: {statement}"
        return statement
