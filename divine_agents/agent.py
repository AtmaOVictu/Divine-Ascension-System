class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Name of the agent.
    state:
        Initial ontological state. One of ``"Ego"``, ``"Jaz"`` or ``"Enotnost"``.
    tension:
        Initial tension level in the range ``[0, 1]``.
    emotion:
        Initial emotion intensity in the range ``[0, 1]``.
    emotion_label:
        Descriptive label for the current emotion (``"neutral"`` by default).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_label: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    def update_emotion(self, value: float, label: str | None = None) -> None:
        """Update emotion intensity and optionally set an emotion label.

        Parameters
        ----------
        value:
            New emotion intensity.
        label:
            Human readable description of the emotion (e.g. ``"fear"``).
        """
        self.emotion = value
        if label is not None:
            self.emotion_label = label
        # Emotion feeds into tension.
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition if emotion or tension thresholds are met."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state and emotion."""
        prefix = ""
        if self.emotion_label == "fear":
            prefix = "(z zaskrbljenostjo) "
        elif self.emotion_label == "joy":
            prefix = "(z veseljem) "
        elif self.emotion_label == "anger":
            prefix = "(z jezo) "

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return prefix + base
