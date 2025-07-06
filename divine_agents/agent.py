class Agent:
    """Ontological agent capable of transitioning philosophical states.

    The agent maintains a current ``state`` (``Ego``, ``Jaz`` or ``Enotnost``),
    a numeric ``tension`` and an ``emotion`` level.  When either ``tension`` is
    above ``0.7`` or ``emotion`` exceeds ``0.5`` the agent will attempt to
    transition to the next state.  ``Ego`` transitions to ``Jaz`` and ``Jaz`` to
    ``Enotnost``.  ``Enotnost`` is considered the final state and will not
    transition further.
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

    # ------------------------------------------------------------------
    # Ontological behaviour
    # ------------------------------------------------------------------

    def philosophical_principle(self) -> str:
        """Return the statement of truth for the current ontological state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    # ------------------------------------------------------------------

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
        """Return a philosophical answer depending on the current state."""
        return self.philosophical_principle()

    def speak(self, question: str) -> str:
        """Return a full dialogue line including state and emotion."""
        principle = self.respond(question)
        return f"{self.name} ({self.state}, emot={self.emotion:.2f}): {principle}"
