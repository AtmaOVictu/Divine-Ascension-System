class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent also contains basic motion properties so that ``motion`` and
    ``emotion`` can be treated independently. Motion is represented with a
    position and speed while emotion influences tension and may affect speed.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, speed: float = 0.0, position: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.speed = speed
        self.position = position
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        # Simple opposition effect: strong emotions speed up motion while
        # subdued emotions slow it down
        if value > 0.5:
            self.speed += value
        else:
            self.speed -= value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def move(self) -> None:
        """Update the agent's position based on current speed."""
        self.position += self.speed

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
