class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name: str
        Name of the agent.
    state: str
        Ontological state (``"Ego"``, ``"Jaz"``, ``"Enotnost"``).
    tension: float
        Current tension level in range ``0-1``.
    emotion: float
        Intensity of the current emotion in range ``0-1``.
    emotion_name: str
        Label for the current emotion (e.g. ``"fear"``, ``"joy"``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_name: str = "neutral") -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, value: float, emotion_name: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            New emotion intensity.
        emotion_name:
            Optional label for the emotion. When provided, tension is adjusted
            according to the emotion type (fear/anger increase it while joy
            decreases it).
        """
        self.emotion = value
        if emotion_name:
            self.emotion_name = emotion_name
            if emotion_name in {"fear", "anger"}:
                self.tension += 0.3
            elif emotion_name == "joy":
                self.tension = max(0.0, self.tension - 0.2)
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
        """Return a philosophical answer depending on the current state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_name == "anger":
            return base + " Govorim z jezo."
        if self.emotion_name == "fear":
            return base + " Čutim strah."
        if self.emotion_name == "joy":
            return base + " Veselim se."
        return base
