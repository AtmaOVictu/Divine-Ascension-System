from .language import LanguageModel


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        language: LanguageModel | None = None,
        agent_id: str | None = None,
    ):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.language = language or LanguageModel("slovenščina", "slv")
        self.agent_id = agent_id or f"EJ-{self.name}"
        self.history = [state]
        self.language_history = [self.language.name]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def change_language(self, new_language: LanguageModel) -> str:
        """Switch to a new language model and confirm the transition."""
        self.language = new_language
        self.language_history.append(new_language.name)
        return new_language.confirm_transition()

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
