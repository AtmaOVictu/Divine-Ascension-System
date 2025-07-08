from .history import History
from .timeline import Timeline
from .space import Space
from .language import Language


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        history: History | None = None,
        time_module: Timeline | None = None,
        space_module: Space | None = None,
        language_module: Language | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.history_module = history if history else History()
        self.time_module = time_module if time_module else Timeline()
        self.space_module = space_module if space_module else Space()
        self.language_module = language_module if language_module else Language()

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.history_module.record(self.name, f"emotion set to {value}")

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.history_module.record(self.name, f"tension set to {value}")

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            self.history_module.record(self.name, f"transitioned to {self.state}")
        self.time_module.tick()
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        base = self.language_module.generate(self.state)
        if self.emotion > 0.5:
            return f"{base} (občuti močna čustva)"
        return base
