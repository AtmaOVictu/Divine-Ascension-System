class Agent:
    """Ontological agent that transitions between philosophical states.

    The agent holds an ontological ``state`` (``Ego``, ``Jaz`` or ``Enotnost``)
    and numerical values for ``tension`` and ``emotion``.  When either the
    tension exceeds ``0.7`` or the emotion exceeds ``0.5`` the agent will move
    to the next ontological state.  ``Ego`` transitions to ``Jaz`` and
    ``Jaz`` transitions to ``Enotnost``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Set emotion intensity and increase tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if emotion or tension exceed thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return an ontological answer influenced by the current emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.7:
            prefix = "Z močnimi čustvi"
        elif self.emotion > 0.3:
            prefix = "Čustveno"
        else:
            prefix = "Mirno"
        return f"{prefix}: {base}"
