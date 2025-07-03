class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Unique identifier for the agent.
    state:
        Current ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension:
        Current tension level of the agent.
    emotion:
        Initial intensity of the agent's emotion.
    emotion_label:
        Label describing the current prevailing emotion (e.g. ``jeza``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_label: str = "nevtralno"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    def update_emotion(self, label: str, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        label:
            Name of the emotion (e.g. ``jeza`` or ``veselje``).
        value:
            Intensity of the emotion in the range ``0.0``-``1.0``.
        """
        self.emotion_label = label
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
        return f"({self.emotion_label}) {base}"
