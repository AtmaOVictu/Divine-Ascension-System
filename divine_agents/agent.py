class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent holds an ontological ``state`` (``Ego``, ``Jaz`` or ``Enotnost``)
    as well as an ``emotion`` intensity and ``emotion_label`` describing the
    current affect. ``tension`` accumulates with emotions and is used to
    determine state transitions.
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

        The agent's ``tension`` increases with the ``value`` to model how
        strong emotions can drive ontological change.
        """
        self.emotion = value
        if label is not None:
            self.emotion_label = label
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded.

        A transition occurs when ``tension`` exceeds ``0.7`` or ``emotion``
        exceeds ``0.5``. ``Ego`` moves to ``Jaz`` and ``Jaz`` moves to
        ``Enotnost``.
        """
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state.

        The wording slightly changes based on the current ``emotion_label`` to
        highlight how emotions colour the agent's perspective.
        """
        prefix = ""
        if self.emotion_label == "anger":
            prefix = "Z jezo pravi: "
        elif self.emotion_label == "fear":
            prefix = "V strahu pravi: "

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return prefix + base
