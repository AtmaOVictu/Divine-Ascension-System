class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Name of the agent.
    state:
        Initial ontological state (``Ego``, ``Jaz``, or ``Enotnost``).
    tension:
        Initial tension level.
    emotion:
        Initial emotion level.
    da:
        Activation flag determining if the agent can transition. ``JA`` is
        interpreted relative to this activation (``DA``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, da: bool = False):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.da = da
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def activate_da(self) -> None:
        """Enable DA so transitions can occur."""
        self.da = True

    def deactivate_da(self) -> None:
        """Disable DA preventing state transitions."""
        self.da = False

    def transition(self) -> str:
        """Perform state transition if thresholds and activation are met."""
        if self.da and (self.tension > 0.7 or self.emotion > 0.5):
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
