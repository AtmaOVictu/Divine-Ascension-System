class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name: str
        Identifier for the agent.
    state: str, optional
        Initial ontological state. Defaults to ``"Ego"``.
    tension: float, optional
        Initial tension level.
    emotion: float, optional
        Initial emotion intensity.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        # keep track of state history for analysis
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and increase tension.

        Parameters
        ----------
        value: float
            New emotion intensity. Higher values increase tension and may
            trigger a state transition during the next :meth:`transition`
            call.
        """
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
        """Return a philosophical answer based on state and emotion."""
        if self.state == "Ego":
            if self.emotion > 0.5:
                return "Resnico vidim kot absolutno in jo branim z vso močjo."
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            if self.emotion > 0.5:
                return "Resnica je relativna in jo obcutim skozi nase odnose."
            return "Resnica je relativna, oblikovana z nasimi odnosi."
        # Enotnost
        if self.emotion > 0.5:
            return "Vse resnice se zlivajo v eno skupno izkusnjo."
        return "Vse resnice so eno, medsebojno povezane."
