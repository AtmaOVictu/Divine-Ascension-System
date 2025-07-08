class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

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

    def start_monologue(self) -> str:
        """Return an introspective monologue when emotion or tension is high.

        The method is triggered when ``tension`` exceeds ``0.7`` or ``emotion``
        exceeds ``0.5``. The returned text reflects the agent's current
        ontological ``state`` along with its emotional context.
        """
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                truth = "Resnica je absolutna in neodvisna od drugih."
            elif self.state == "Jaz":
                truth = "Resnica je relativna, oblikovana z našimi odnosi."
            else:
                truth = "Vse resnice so eno, medsebojno povezane."
            return (
                f"{self.name} razmišlja: {truth} "
                f"(Čustva={self.emotion:.2f}, napetost={self.tension:.2f})"
            )
        return ""
