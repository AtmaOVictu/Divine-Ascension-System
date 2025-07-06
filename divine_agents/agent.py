class Agent:
    """Represent an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Unique agent name used in dialogue output.
    state:
        Initial ontological state (``"Ego"``, ``"Jaz"`` or ``"Enotnost"``).
    tension:
        Current tension level. When it rises above ``0.7`` a transition may
        occur.
    emotion:
        Current emotion intensity. Values greater than ``0.5`` can also trigger
        a transition.
    emotion_type:
        Describes the prevailing emotion (``"fear"``, ``"joy"``, ``"anger"`` ...).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and optionally its type.

        Parameters
        ----------
        value:
            New emotion intensity.
        emotion_type:
            Name of the emotion influencing the agent (e.g. ``"fear"``).
        """
        self.emotion = value
        if emotion_type is not None:
            self.emotion_type = emotion_type
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
        """Return a philosophical answer influenced by state and emotion."""
        emotion_prefix = {
            "fear": "V strahu verjamem, da",
            "joy": "Radostno verjamem, da",
            "anger": "Z jezo trdim, da",
        }.get(self.emotion_type, "Verjamem, da")

        if self.state == "Ego":
            base = "resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "vse resnice so eno, medsebojno povezane."

        return f"{emotion_prefix} {base}"
