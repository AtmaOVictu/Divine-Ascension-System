class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent maintains an ontological ``state`` (``Ego``, ``Jaz`` or
    ``Enotnost``) and numerical values for ``tension`` and ``emotion``.  When
    either of these values crosses their respective threshold (tension > 0.7 or
    emotion > 0.5) the agent will transition to the next state.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0):
        """Create an agent.

        Parameters
        ----------
        name:
            Display name of the agent.
        state:
            Initial ontological state (defaults to ``"Ego"``).
        tension:
            Initial tension level.
        emotion:
            Initial emotion intensity.
        """
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension = min(1.0, self.tension + value)

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

        The emotional intensity modifies the tone of the answer: if
        ``emotion`` is greater than ``0.5`` the agent replies with emphasis.
        """
        intense = self.emotion > 0.5

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return base + ("" if not intense else " Čutim močna čustva.")
