class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent holds an ontological ``state`` (``Ego``, ``Jaz`` or ``Enotnost``)
    and numerical values for ``tension`` and ``emotion``.  A transition is
    triggered whenever ``tension`` is greater than ``0.7`` or ``emotion`` is
    greater than ``0.5``.  ``update_emotion`` automatically increases
    ``tension`` which allows emotional build-up to influence state changes.
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
        """Return a philosophical answer influenced by the current state and emotion."""
        prefix = "Umirjeno" if self.emotion < 0.3 else "Strastno" if self.emotion > 0.7 else "Premišljeno"
        if self.state == "Ego":
            text = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            text = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            text = "Vse resnice so eno, medsebojno povezane."
        return f"{prefix} odgovarjam: {text}"
