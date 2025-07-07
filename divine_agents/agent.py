class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name: str
        Identifier of the agent.
    state: str, optional
        Starting ontological state (default ``"Ego"``).
    tension: float, optional
        Initial tension level.
    emotion: float, optional
        Initial emotion intensity.
    emotion_type: str, optional
        Descriptor of the prevailing emotion (e.g. ``"fear"``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral") -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and optionally its descriptor.

        Increasing emotion will raise the internal tension as well.
        """
        self.emotion = value
        if emotion_type is not None:
            self.emotion_type = emotion_type
        # emotion directly influences tension
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

        The emotional descriptor influences the tone of the response.
        """
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_type == "fear":
            prefix = "Strah me je, toda "
        elif self.emotion_type == "anger":
            prefix = "Jezen sem, vendar "
        elif self.emotion_type == "joy":
            prefix = "Vesel sem, in "
        else:
            prefix = ""

        return prefix + base
