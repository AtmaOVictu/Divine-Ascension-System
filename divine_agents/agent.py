class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.current_emotion = ""
        self.history = [state]

    def set_emotion(self, name: str, intensity: float) -> None:
        """Set emotion name and intensity, adjusting tension accordingly."""
        self.current_emotion = name
        self.emotion = intensity
        self.tension += intensity

    def update_emotion(self, value: float) -> None:
        """Compatibility wrapper to set unnamed emotion level."""
        self.set_emotion("", value)

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
        prefix = ""
        if self.emotion > 0.7:
            prefix = f"Z veliko {self.current_emotion} povem: "
        elif self.emotion > 0.4:
            prefix = f"Z občutkom {self.current_emotion} povem: "

        if self.state == "Ego":
            principle = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            principle = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            principle = "Vse resnice so eno, medsebojno povezane."
        return prefix + principle

