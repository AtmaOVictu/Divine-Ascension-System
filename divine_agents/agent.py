class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent tracks an internal ``time`` counter that is increased whenever
    emotion, tension or state changes occur. Each entry in ``history`` records
    the time step alongside the state so tests can assert correct progression
    over time.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.time = 0
        self.history = [(self.time, state)]

    def advance_time(self, delta: int = 1) -> None:
        """Increase the internal time counter."""
        self.time += delta

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.advance_time()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.advance_time()

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.advance_time()
        self.history.append((self.time, self.state))
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
