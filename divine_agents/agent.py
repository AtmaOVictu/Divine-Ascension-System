class Agent:
    """Represents an ontological agent capable of transitioning states.

    An agent holds a current ontological ``state`` (``Ego``, ``Jaz`` or
    ``Enotnost``), an emotional ``tension`` level and an ``emotion`` intensity.
    The ``emotion_label`` describes the current dominating emotion (e.g.
    ``anger`` or ``joy``). State transitions occur when either ``tension`` is
    greater than ``0.7`` or ``emotion`` intensity is greater than ``0.5``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_label: str = "neutral"):
        """Create a new ``Agent``.

        Parameters
        ----------
        name:
            Name of the agent.
        state:
            Initial ontological state.
        tension:
            Initial tension level.
        emotion:
            Initial emotion intensity in range ``0``-``1``.
        emotion_label:
            Descriptive label of the current emotion.
        """
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    def set_emotion(self, label: str, value: float) -> None:
        """Update emotion label and intensity.

        ``tension`` is increased by ``value`` to reflect the emotional impact.
        """
        self.emotion_label = label
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition if emotion or tension exceed thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state.

        The answer is coloured by the agent's current ``emotion_label``.
        """
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_label and self.emotion_label != "neutral":
            return f"{base} ({self.emotion_label})"
        return base
