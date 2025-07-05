class Agent:
    """Represent an ontological agent capable of transitioning states.

    The agent tracks ``tension`` and ``emotion`` values which influence
    transitions between the philosophical states ``Ego`` -> ``Jaz`` ->
    ``Enotnost``.  In addition, the agent records how long it has been in the
    current state (``time_duration``) and whether it is stagnant
    (``lenobe``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.time_duration = 0
        self.lenobe = 0

    def update(self) -> None:
        """Update duration counters and determine stagnation (lenobe)."""
        self.time_duration += 1
        if self.tension < 0.1 and self.emotion < 0.1:
            self.lenobe = 1
        else:
            self.lenobe = 0

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
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.7:
            return base + " Čutim močna čustva, kar krepi moje prepričanje."
        if self.emotion > 0.3:
            return base + " Čustveno sem vznemirjen."
        return base
