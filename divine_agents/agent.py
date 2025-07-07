class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        """Create a new agent.

        Parameters
        ----------
        name:
            Agent identifier.
        state:
            Initial ontological state.
        tension:
            Initial tension level (0-1).
        emotion:
            Initial emotion level (0-1).
        """
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Increase emotion intensity and adjust tension.

        Parameters
        ----------
        value:
            Value by which the current emotion increases.
        """
        self.emotion = max(0.0, min(1.0, self.emotion + value))
        self.tension = max(0.0, min(1.0, self.tension + value))

    def update_tension(self, value: float) -> None:
        """Directly set tension level (clamped between 0 and 1)."""
        self.tension = max(0.0, min(1.0, value))

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
        """Return a philosophical answer influenced by state and emotion."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }
        reply = base.get(self.state, "")
        if self.emotion > 0.5:
            reply = f"{reply} (čustveno)"
        return reply
