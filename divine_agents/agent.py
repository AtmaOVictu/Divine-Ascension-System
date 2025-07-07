class Agent:
    """Ontological agent that transitions between philosophical states.

    The agent keeps track of its emotional intensity and tension level.
    Once either the tension exceeds ``0.7`` or the emotion exceeds ``0.5``
    the agent progresses through the states ``Ego`` -> ``Jaz`` -> ``Enotnost``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    PHILOSOPHY = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Increase emotion intensity and adjust tension accordingly."""
        self.emotion += value
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
        """Return a philosophical answer influenced by the agent's emotion."""
        base = self.PHILOSOPHY.get(self.state, "")
        if self.emotion > 0.5:
            mood = "Moja custva so mocna."  # strong emotion
        elif self.emotion > 0:
            mood = "Custva rahlo vplivajo."  # mild emotion
        else:
            mood = "Brez custvenega odziva."  # no emotion
        return f"{base} {mood}"

