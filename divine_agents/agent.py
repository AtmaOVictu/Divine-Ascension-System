class Agent:
    """Ontological agent capable of transitioning philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    COLORS = {
        "Ego": "\033[91m",       # red
        "Jaz": "\033[93m",       # yellow
        "Enotnost": "\033[92m",  # green
    }
    RESET = "\033[0m"

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_name: str = "neutral",
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def set_emotion(self, name: str, value: float) -> None:
        """Set named emotion and update tension."""
        self.emotion_name = name
        self.update_emotion(value)

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
        return f"{base} ({self.emotion_name})"

    def colored_state(self) -> str:
        """Return ANSI colored state name for console output."""
        return f"{self.COLORS.get(self.state, '')}{self.state}{self.RESET}"
