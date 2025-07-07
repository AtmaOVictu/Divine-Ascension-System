class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Display name for the agent.
    state:
        Current ontological state. One of ``Ego``, ``Jaz`` or ``Enotnost``.
    tension:
        Current tension level ``[0, 1]``.
    emotion:
        Current emotion intensity ``[0, 1]``.
    emotion_type:
        Name of the active emotion (e.g. ``jeza`` or ``strah``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type or ""
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            New emotion intensity ``[0, 1]``.
        emotion_type:
            Optional name of the emotion influencing the agent.
        """
        self.emotion = value
        self.tension += value
        if emotion_type is not None:
            self.emotion_type = emotion_type

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

        The response is coloured by the current emotion type if defined.
        """
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_type:
            return f"{base} Moje čustvo je {self.emotion_type}."
        return base
