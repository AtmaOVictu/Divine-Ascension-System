class Agent:
    """Represents an ontological agent capable of transitioning states."""

    # Extended states including the RES phases for deeper transitions
    STATES = (
        "Ego",
        "RES000",
        "RES001",
        "RES002",
        "RES003",
        "Jaz",
        "Enotnost",
    )

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
                self.state = "RES000"
            elif self.state == "RES000":
                self.state = "RES001"
            elif self.state == "RES001":
                self.state = "RES002"
            elif self.state == "RES002":
                self.state = "RES003"
            elif self.state == "RES003":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "RES000":
            return "Začetno stabilno stanje odpira pot spremembi."
        if self.state == "RES001":
            return "Oblikuje se začetna harmonija med vsemi deli sistema."
        if self.state == "RES002":
            return "Napetosti povzročajo začetno transformacijo."
        if self.state == "RES003":
            return "Dosežena je popolna realizacija elementov."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
