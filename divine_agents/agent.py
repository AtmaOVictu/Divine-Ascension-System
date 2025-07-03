class Agent:
    """Ontological agent capable of transitioning between states.

    Parameters
    ----------
    name:
        Human readable identifier for the agent.
    state:
        Initial ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension:
        Starting tension level.
    emotion:
        Starting emotional intensity.
    emotion_label:
        Name of the current emotion (e.g. ``fear`` or ``joy``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_label: str = "neutral",
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    def update_emotion(self, value: float, label: str) -> None:
        """Update emotional intensity and adjust tension.

        Parameters
        ----------
        value:
            New emotion intensity in range ``0`` to ``1``.
        label:
            Description of the emotion (``fear``, ``joy``...).
        """

        self.emotion = value
        self.emotion_label = label
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
            return (
                "Resnica je absolutna in neodvisna od drugih "
                f"(čustvo: {self.emotion_label})."
            )
        if self.state == "Jaz":
            return (
                "Resnica je relativna, oblikovana z našimi odnosi "
                f"(čustvo: {self.emotion_label})."
            )
        return (
            "Vse resnice so eno, medsebojno povezane "
            f"(čustvo: {self.emotion_label})."
        )
