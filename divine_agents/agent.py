from .translator import Translator


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, language: str = "sl"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.language = language
        self.history = [state]
        self.tasks = []
        self.translator = Translator()

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

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
        translated = self.translator.response(self.state, self.language)
        if translated:
            return translated
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def accept_task(self, task: str, language: str | None = None) -> str:
        """Translate a task and store it for later processing."""
        lang = language or self.language
        translated = self.translator.translate(task, lang)
        self.tasks.append(translated)
        return translated
