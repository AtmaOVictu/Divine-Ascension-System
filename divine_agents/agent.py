from .temperature import temperature_to_color


class Agent:
    """Represents an ontological agent capable of transitioning states.

    An agent can update its emotional state and tension, which may trigger
    transitions between philosophical phases. Temperature is used as a simple
    metaphor for the agent's energetic state and is visualised with colours.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, temperature: float = 20.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.temperature = temperature
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity, tension and temperature."""
        self.emotion = value
        self.tension += value
        self.temperature = 20 + 30 * value

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

    @property
    def color(self):
        """Return RGB colour representing current temperature."""
        return temperature_to_color(self.temperature)

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
