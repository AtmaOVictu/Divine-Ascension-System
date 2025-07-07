class Agent:
    """Ontological agent capable of transitioning states based on emotions.

    Attributes
    ----------
    name: str
        Agent identifier.
    state: str
        Current ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension: float
        Accumulated tension driving potential transitions.
    emotion: float
        Current emotional intensity.
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

    def _emotion_descriptor(self) -> str:
        """Return a short descriptor based on current emotional intensity."""
        return "strastno" if self.emotion > 0.5 else "mirno"

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        prefix = f"{self._emotion_descriptor()} odgovori: "
        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."
