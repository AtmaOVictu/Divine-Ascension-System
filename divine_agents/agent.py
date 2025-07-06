class Agent:
    """Represents an ontological agent with emotional state and transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTIONS = ("fear", "joy", "anger")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotions=None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions = emotions or {emotion: 0.0 for emotion in self.EMOTIONS}
        self.history = [state]

    def set_emotion(self, emotion: str, value: float) -> None:
        """Set the intensity of a given emotion and adjust tension."""
        if emotion in self.emotions:
            self.emotions[emotion] = value
            self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def max_emotion(self) -> float:
        """Return the highest emotion value."""
        return max(self.emotions.values()) if self.emotions else 0.0

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.max_emotion() > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by current emotions."""
        tone = ""
        if self.emotions.get("fear", 0) > 0.5:
            tone = " (v strahu)"
        elif self.emotions.get("joy", 0) > 0.5:
            tone = " (veselo)"
        elif self.emotions.get("anger", 0) > 0.5:
            tone = " (jezno)"

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return base + tone
