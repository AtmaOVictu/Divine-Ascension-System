class Agent:
    """Ontological agent capable of transitioning states.

    The agent moves between ``Ego``, ``Jaz`` and ``Enotnost`` depending on
    internal emotion and tension levels.  Transitions occur when ``tension``
    exceeds ``0.7`` or ``emotion`` exceeds ``0.5``.
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
        """Return a philosophical answer depending on the current state.

        The returned text also reflects the agent's emotional level.
        """
        descriptor = self._emotion_descriptor()
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{descriptor} {base}"

    def _emotion_descriptor(self) -> str:
        """Return a short textual description of the current emotion."""
        if self.emotion > 0.7:
            return "Z veliko strastjo"
        if self.emotion > 0.5:
            return "Z navdusenjem"
        if self.emotion > 0.3:
            return "Zmerno"
        return "Mirno"

