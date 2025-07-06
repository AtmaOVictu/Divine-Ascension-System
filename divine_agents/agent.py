"""Base agent implementation used across the package."""


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0, emotion: float = 0.0,
                 emotion_name: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name or "neutral"
        self.history: list[str] = [state]

    def feel(self, emotion_name: str, intensity: float) -> None:
        """Record an emotion and adjust tension accordingly."""
        self.emotion_name = emotion_name
        self.emotion = intensity
        self.tension += intensity

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
        """Return a philosophical answer depending on the current state and emotion."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        modifier_map = {
            "fear": "S strahom povem, ",
            "joy": "Z veseljem povem, ",
            "anger": "Z jezo trdim, ",
        }

        if self.emotion > 0.5 and self.emotion_name in modifier_map:
            return modifier_map[self.emotion_name] + base
        return base
