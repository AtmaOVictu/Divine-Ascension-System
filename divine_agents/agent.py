class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Identifier for the agent.
    state:
        Initial ontological state.
    tension:
        Current tension level influencing transitions.
    emotion:
        Numeric intensity of the current emotion.
    emotion_name:
        Name of the emotion currently experienced.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_name: str = "neutral") -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, name: str, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        name:
            The emotion currently felt (e.g. ``fear`` or ``joy``).
        value:
            Intensity of the emotion in the range ``0.0-1.0``.
        """
        self.emotion_name = name
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

    @property
    def philosophical_principle(self) -> str:
        """Return the philosophical principle associated with the state."""
        if self.state == "Ego":
            return "Truth is absolute and independent of others."
        if self.state == "Jaz":
            return "Truth is relative, shaped by relationships."
        return "All truths are one and interconnected."

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} (čustvo: {self.emotion_name})"
