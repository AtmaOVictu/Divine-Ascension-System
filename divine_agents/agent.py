class Agent:
    """Ontological agent capable of state transitions and dialogue."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.lenobe = 0
        self.time_duration = 0
        self.max_values = (1.0, 1.0, 1.0, 1.0)

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update(self) -> None:
        """Increment time duration and update lenobe flag."""
        self.time_duration += 1
        if self.tension < 0.1 and self.emotion < 0.1:
            self.lenobe = 1
        else:
            self.lenobe = 0

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if tension or emotion exceed thresholds."""
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

    # Helper accessors used in tests
    def get_state(self) -> str:
        return self.state

    def get_time_duration(self) -> int:
        return self.time_duration

    def get_lenobe(self) -> int:
        return self.lenobe

    def f_error(self) -> float:
        total = (
            self.tension / self.max_values[0]
            + self.emotion / self.max_values[1]
            + 0 / self.max_values[2]
            + 0 / self.max_values[3]
        )
        return abs(total - 1)
