class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name: str
        Name of the agent.
    state: str
        Initial ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension: float
        Initial tension level in range ``0.0``-``1.0``.
    emotion: float
        Initial emotional intensity in range ``0.0``-``1.0``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    PRINCIPLES = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

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
        previous = self.state
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by current emotion."""
        base = self.PRINCIPLES[self.state]
        if self.emotion > 0.7:
            mood = "Iz intenzivnih custev povem, da "
        elif self.emotion > 0.5:
            mood = "Z jezo dodajam, da "
        elif self.emotion > 0.2:
            mood = "Čustveno pravim, da "
        else:
            mood = ""
        return mood + base if mood else base
