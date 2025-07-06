class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = ""
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def feel(self, name: str, intensity: float) -> None:
        """Apply a named emotion which influences tension."""
        self.emotion_name = name
        self.emotion = intensity
        if name in {"fear", "anger"}:
            self.tension += intensity
        elif name == "joy":
            self.tension = max(0.0, self.tension - intensity / 2)
        else:
            self.tension += intensity / 2
        # clamp tension to [0, 1]
        self.tension = max(0.0, min(self.tension, 1.0))

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
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        mood = ""
        if self.emotion_name == "fear":
            mood = " Čutim strah."
        elif self.emotion_name == "anger":
            mood = " Čutim jezo."
        elif self.emotion_name == "joy":
            mood = " Občutim radost."
        return base + mood

