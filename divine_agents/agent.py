class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Identifier for the agent.
    state:
        Initial ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension:
        Current tension level. When it rises above ``0.7`` it can trigger a
        state transition.
    emotion_level:
        Numeric intensity of the current emotion. If it exceeds ``0.5`` it may
        also trigger a state transition.
    emotion:
        Name of the emotion (e.g. ``fear``, ``joy``) used in dialogue.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0,
                 emotion_level: float = 0.0, emotion: str = "neutral") -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_level = emotion_level
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float, *, emotion: str | None = None) -> None:
        """Update emotion intensity and optionally set emotion name.

        Parameters
        ----------
        value:
            New emotional intensity.
        emotion:
            Name of the emotion associated with ``value``.
        """
        self.emotion_level = value
        if emotion is not None:
            self.emotion = emotion
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        prefix = f"({self.emotion}) " if self.emotion != "neutral" else ""
        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."
