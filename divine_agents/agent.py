try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except Exception:  # pragma: no cover - fallback when colorama is missing
    class Fore:
        RED = ""
        YELLOW = ""
        GREEN = ""

    class Style:
        RESET_ALL = ""

    def init(*args, **kwargs):
        return None


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion_level: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_level = emotion_level
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, level: float, emotion: str) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion_level = level
        self.emotion_type = emotion
        self.tension += level

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        emotion_prefix = {
            "joy": "Z veseljem",
            "fear": "S strahom",
            "anger": "Z jezo",
        }.get(self.emotion_type, "")

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return f"{emotion_prefix} {base}".strip()

    def colored_state(self) -> str:
        """Return the current state wrapped in color codes."""
        color_map = {
            "Ego": Fore.RED,
            "Jaz": Fore.YELLOW,
            "Enotnost": Fore.GREEN,
        }
        return f"{color_map.get(self.state, '')}{self.state}{Style.RESET_ALL}"
