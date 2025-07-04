class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent holds an ontological ``state`` and keeps track of ``tension`` and
    ``emotion`` levels.  When either the tension exceeds ``0.7`` or the emotion
    exceeds ``0.5`` the agent transitions to the next ontological state.  The
    valid states are defined in ``STATES`` and ordered according to the
    philosophical progression ``Ego`` → ``Jaz`` → ``Enotnost``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_label: str | None = None) -> None:
        """Create a new agent.

        Parameters
        ----------
        name:
            Name of the agent.
        state:
            Initial ontological state. Must be one of :pyattr:`STATES`.
        tension:
            Initial tension level.
        emotion:
            Initial emotion intensity.
        emotion_label:
            Optional textual label describing the current emotion (e.g.
            ``"fear"`` or ``"joy"``).  This value influences the textual
            response of the agent.
        """

        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label or "neutral"
        self.history = [state]

    def update_emotion(self, value: float, label: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            New emotion intensity (``0``-``1``).
        label:
            Optional label describing the emotion which will be stored on the
            agent for later use in dialogue.
        """

        self.emotion = value
        if label:
            self.emotion_label = label
        # Emotion naturally contributes to the feeling of tension.
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition if thresholds are exceeded.

        The transition order follows :pyattr:`STATES`.  The current state is
        appended to :pyattr:`history` each time this method is called, even if
        no transition occurs.
        """
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        emotion_part = ""
        if self.emotion_label == "fear":
            emotion_part = " Občutim strah."
        elif self.emotion_label == "joy":
            emotion_part = " Napolnjuje me veselje."
        elif self.emotion_label == "anger":
            emotion_part = " Preveva me jeza."

        return f"{base}{emotion_part}"
