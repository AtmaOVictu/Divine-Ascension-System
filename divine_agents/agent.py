class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Agent name used in dialogues.
    state:
        Initial ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension:
        Current tension level. Values above ``0.7`` may trigger a state
        transition.
    emotion:
        Current emotion intensity. Values above ``0.5`` may also trigger a
        transition and colour the agent's responses.
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
        """Return a textual description of the current emotional intensity."""
        if self.emotion > 0.7:
            return "strastno"
        if self.emotion < 0.2:
            return "mirno"
        return "uravnoteženo"

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state
        coloured by current emotional intensity."""
        mood = self._emotion_descriptor()
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} ({mood})"
