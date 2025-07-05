class Agent:
    """Represents an ontological agent capable of transitioning states.

    Each agent tracks its current ``state`` (``Ego``, ``Jaz`` or ``Enotnost``),
    the current level of ``tension`` and ``emotion``.  State transitions occur
    when either the tension exceeds ``0.7`` or the emotion exceeds ``0.5``.
    ``history`` keeps a record of all visited states.
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

        The returned string also reflects the agent's current emotional
        disposition, which subtly alters the phrasing of the answer.
        """
        emotion = self._emotion_descriptor()
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} (Čustvo: {emotion})"

    def _emotion_descriptor(self) -> str:
        """Map the current emotion value to a descriptive word."""
        if self.emotion > 0.5:
            return "strastno"
        if self.emotion < -0.2:
            return "jezno"
        return "mirno"
