class Agent:
    """Ontological agent capable of emotional state transitions.

    Parameters
    ----------
    name:
        Name of the agent.
    state:
        Initial ontological state (``"Ego"`` by default).
    tension:
        Initial tension value.
    emotion:
        Initial emotional intensity.
    """

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

    def speak(self, question: str) -> str:
        """Return formatted response including agent name and state."""
        answer = self.respond(question)
        return f"{self.name} ({self.state}): {answer}"

    def __repr__(self) -> str:  # pragma: no cover - convenience only
        return f"Agent(name={self.name!r}, state={self.state!r}, tension={self.tension}, emotion={self.emotion})"
