class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        The agent's identifier.
    state:
        Initial ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension:
        Level of internal tension used for triggering transitions.
    emotion:
        Numerical representation of current emotional intensity.
    mood:
        Qualitative emotion description (e.g. ``fear``, ``joy``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, mood: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.mood = mood
        self.history = [state]

    def update_emotion(self, value: float, mood: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            Intensity of the emotion. Higher values increase ``tension``.
        mood:
            Optional textual description of the emotion (e.g. ``fear`` or
            ``joy``). If provided, :attr:`mood` will be updated.
        """
        self.emotion = value
        if mood is not None:
            self.mood = mood
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
        """Return a philosophical answer depending on the current state.

        The returned string also reflects the agent's current mood if it is
        not neutral.
        """
        mood_note = f" Čutim {self.mood}." if self.mood != "neutral" else ""
        if self.state == "Ego":
            return (
                "Resnica je absolutna in neodvisna od drugih." + mood_note
            )
        if self.state == "Jaz":
            return (
                "Resnica je relativna, oblikovana z našimi odnosi." + mood_note
            )
        return "Vse resnice so eno, medsebojno povezane." + mood_note
