"""Core agent model used throughout the library."""


class Colors:
    """ANSI color codes used for terminal output."""

    RED = "\033[31m"
    YELLOW = "\033[33m"
    GREEN = "\033[32m"
    RESET = "\033[0m"


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    TENSION_THRESHOLD = 0.7
    EMOTION_THRESHOLD = 0.5

    COLOR_MAP = {
        "Ego": Colors.RED,
        "Jaz": Colors.YELLOW,
        "Enotnost": Colors.GREEN,
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > self.TENSION_THRESHOLD or self.emotion > self.EMOTION_THRESHOLD:
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

    # Helper utilities -----------------------------------------------------

    def color(self) -> str:
        """Return ANSI color associated with the current state."""
        return self.COLOR_MAP.get(self.state, Colors.RESET)

    def speak(self, question: str) -> str:
        """Return a colorised philosophical response."""
        response = self.respond(question)
        return f"{self.color()}{self.name} ({self.state}): {response}{Colors.RESET}"
