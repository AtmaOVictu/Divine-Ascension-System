class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Name of the agent.
    state:
        Current ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension:
        Current tension level that may trigger state transitions.
    emotion:
        Intensity of the current emotion ``[0, 1]``.
    emotion_type:
        Optional textual description of the emotion (e.g. ``fear`` or ``joy``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, kind: str | None = None) -> None:
        """Update emotion intensity and optionally set its type.

        Parameters
        ----------
        value:
            New emotion intensity in the range ``[0, 1]``.
        kind:
            Optional name of the emotion (e.g. ``jeza``).
        """
        self.emotion = value
        if kind is not None:
            self.emotion_type = kind
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
        """Return a philosophical answer influenced by the current state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        if self.emotion_type and self.emotion_type != "neutral":
            base += f" Čutim {self.emotion_type}."
        return base
