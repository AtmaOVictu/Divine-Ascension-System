from .context import Context


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 context: Context | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.context = context or Context()
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def set_context(self, inner: str, outer: str, philosophy: str = "") -> None:
        """Assign contextual influences to the agent."""
        self.context.inner = inner
        self.context.outer = outer
        self.context.philosophy = philosophy

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def contextual_transition(self) -> str:
        """Transition based on the currently assigned context."""
        if self.context.inner == "visoka napetost" and self.context.outer == "stresno okolje":
            self.update_tension(0.8)
            self.update_emotion(0.6)
        elif self.context.inner == "mirno" and self.context.outer == "podpora":
            self.update_tension(1.0)
            self.update_emotion(1.0)
        return self.transition()

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        base = ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            return f"{base} (čustveno)"
        return base
