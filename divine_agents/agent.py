class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTION_TYPES = ("generic", "fear", "joy", "anger")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        # Track individual emotion intensities
        self.emotions = {etype: 0.0 for etype in self.EMOTION_TYPES}
        self.emotions["generic"] = emotion

    def update_emotion(self, value: float, emotion_type: str = "generic") -> None:
        """Update emotion intensity and adjust tension accordingly."""
        if emotion_type not in self.emotions:
            self.emotions[emotion_type] = 0.0
        self.emotions[emotion_type] = value
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or any(v > 0.5 for v in self.emotions.values()):
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            reply = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            reply = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            reply = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            reply += " Čutim močna čustva, ki vplivajo na mojo percepcijo."
        return reply
