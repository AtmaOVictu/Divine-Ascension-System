class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Identifier of the agent.
    state:
        Initial ontological state (Ego, Jaz, or Enotnost).
    tension:
        Initial tension level.
    emotion:
        Initial emotion intensity.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_label: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    def update_emotion(self, value: float, label: str | None = None) -> None:
        """Update emotion intensity, label and adjust tension.

        Negative emotions such as ``fear`` or ``anger`` increase tension
        slightly more, while ``joy`` reduces it a bit.
        """
        self.emotion = value
        if label is not None:
            self.emotion_label = label

        influence = 0.0
        if self.emotion_label in {"fear", "anger"}:
            influence = 0.2
        elif self.emotion_label == "joy":
            influence = -0.1

        self.tension += value + influence

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
        prefix = ""
        if self.emotion_label == "anger":
            prefix = "(z jezo) "
        elif self.emotion_label == "joy":
            prefix = "(z veseljem) "
        elif self.emotion_label == "fear":
            prefix = "(v strahu) "

        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."
