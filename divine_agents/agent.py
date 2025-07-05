from .language import LANGUAGE_MODELS


class Agent:
    """Represents an ontological agent capable of transitioning states and languages."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        language: str = "sloven\u0161\u010dina",
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.language = language
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
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state and language."""
        model = LANGUAGE_MODELS.get(self.language)
        if not model:
            return ""
        return model.response(self.state)

    def change_language(self, language: str) -> None:
        """Change the agent's active language if available."""
        if language in LANGUAGE_MODELS:
            self.language = language
