"""Core agent primitives used in philosophical simulations."""

class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Name of the agent.
    state:
        Current ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension:
        Level of internal tension. Values above ``0.7`` may trigger a
        state transition.
    emotion:
        Intensity of the agent's current emotion. Values above ``0.5``
        also trigger transitions.
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
        """Return a philosophical answer influenced by emotion and state."""
        intense = self.emotion > 0.5
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
            if intense:
                return base + " Ne strinjam se s tvojimi dvomi!"
            return base
        if self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
            if intense:
                return base + " Vsak od nas jo vidi po svoje."
            return base
        base = "Vse resnice so eno, medsebojno povezane."
        if intense:
            return base + " Čutim globoko povezanost."
        return base
