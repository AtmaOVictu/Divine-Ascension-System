class Agent:
    """Represents an ontological agent capable of transitioning states.

    Attributes
    ----------
    name : str
        Agent identifier.
    state : str
        Current ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension : float
        Accumulated tension driving potential transitions.
    emotion : float
        Current emotional intensity.
    temperature : float
        Environmental or internal temperature affecting the agent.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, temperature: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.temperature = temperature
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    @staticmethod
    def temperature_to_color(temperature: float) -> str:
        """Map a temperature value to a color name."""
        if temperature < 0:
            return "blue"
        if 0 <= temperature < 25:
            return "green"
        if 25 <= temperature < 50:
            return "yellow"
        return "red"

    def update_temperature(self, value: float) -> str:
        """Update temperature and return the mapped color."""
        self.temperature = value
        return self.temperature_to_color(value)

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
