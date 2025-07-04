class Agent:
    """Ontological agent that transitions through philosophical states.

    The agent's ``state`` can be one of ``Ego``, ``Jaz`` or ``Enotnost`` and
    is influenced by its ``tension`` and ``emotion`` levels.  When ``tension`` is
    greater than ``0.7`` or ``emotion`` exceeds ``0.5`` the agent will attempt to
    move from ``Ego`` to ``Jaz`` or from ``Jaz`` to ``Enotnost``.  ``Enotnost`` is
    a terminal state in this simple model.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Adjust emotion intensity and accumulate tension.

        Parameters
        ----------
        value: float
            Change in emotional intensity. The resulting emotion is clamped to
            the interval ``[0.0, 1.0]``.
        """
        self.emotion = max(0.0, min(1.0, self.emotion + value))
        self.tension = max(0.0, min(1.0, self.tension + value))

    def update_tension(self, value: float) -> None:
        """Directly set tension level within ``[0.0, 1.0]``."""
        self.tension = max(0.0, min(1.0, value))

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
        if self.emotion > 0.7:
            mood = "Strastno"
        elif self.emotion > 0.3:
            mood = "Premi\u0161ljeno"
        else:
            mood = "Mirno"

        if self.state == "Ego":
            answer = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            answer = "Resnica je relativna, oblikovana z na\u0161imi odnosi."
        else:
            answer = "Vse resnice so eno, medsebojno povezane."

        return f"{mood}: {answer}"

