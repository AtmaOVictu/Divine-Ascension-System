class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name: str
        Identifier for the agent.
    state: str
        Initial ontological state. One of ``Ego``, ``Jaz`` or ``Enotnost``.
    tension: float
        Initial tension level.
    emotion: float
        Initial emotion intensity.
    emotion_type: str
        Descriptive name of the current emotion (e.g. ``jeza`` or ``veselje``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, emotion_type: str = "nevtralno") -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and optionally its descriptive type.

        Parameters
        ----------
        value:
            New emotion intensity.
        emotion_type:
            Optional description of the emotion (e.g. ``jeza``).
        """
        self.emotion = value
        if emotion_type is not None:
            self.emotion_type = emotion_type
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
        """Return a philosophical answer depending on the current state.

        The answer also reflects the current emotional stance of the agent.
        """
        if self.state == "Ego":
            truth = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            truth = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            truth = "Vse resnice so eno, medsebojno povezane."

        return f"{truth} Čutim {self.emotion_type}."

