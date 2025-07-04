class Agent:
    """Ontological agent that transitions through philosophical states.

    The agent holds an emotional intensity and tension level which influence
    transitions between the states ``Ego``, ``Jaz`` and ``Enotnost``.  A
    transition occurs when either ``tension`` exceeds ``0.7`` or ``emotion``
    exceeds ``0.5``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Set the emotional intensity and adjust tension accordingly."""
        self.emotion = value
        # Emotions heighten the overall tension of the agent.
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition if threshold conditions are met."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    # ------------------------------------------------------------------
    # Dialogue utilities
    # ------------------------------------------------------------------
    def _emotion_descriptor(self) -> str:
        """Return a short description based on current emotional intensity."""
        if self.emotion > 0.7:
            return "z intenzivnimi čustvi"
        if self.emotion > 0.3:
            return "s čustvenim tonom"
        return "mirno"

    def respond(self, question: str) -> str:
        """Return a philosophical answer based on current state and emotion."""
        prefix = self._emotion_descriptor()
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{prefix}, {base}"
