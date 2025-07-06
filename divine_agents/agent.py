class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.harmony = False
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        if emotion_type is not None:
            self.emotion_type = emotion_type
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def check_harmony(self) -> bool:
        """Return True when state and emotion type are in harmony."""
        if self.state == "Ego" and self.emotion_type == "calm":
            self.harmony = True
        elif self.state == "Jaz" and self.emotion_type == "joyful":
            self.harmony = True
        elif self.state == "Enotnost" and self.emotion_type in {"peaceful", "serene"}:
            self.harmony = True
        else:
            self.harmony = False
        return self.harmony

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded and harmony exists."""
        if (self.tension > 0.7 or self.emotion > 0.5) and self.check_harmony():
            if self.state == "Ego" and self.harmony:
                self.state = "Jaz"
            elif self.state == "Jaz" and self.harmony:
                self.state = "Enotnost"
            elif self.state == "Enotnost" and self.harmony:
                self.state = "Ego"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def display_state(self) -> str:
        """Return a human readable description of the current state and tension."""
        return (
            f"Agent {self.name} je v stanju {self.state} z napetostjo {self.tension:.2f}."
        )
