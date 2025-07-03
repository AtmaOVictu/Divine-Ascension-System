class Agent:
    """Represent an ontological agent capable of transitioning states.

    Each agent maintains a current ontological ``state`` (``Ego``,
    ``Jaz`` or ``Enotnost``), a ``tension`` level and an ``emotion``
    intensity.  The ``emotion_type`` attribute describes the dominating
    feeling (e.g. ``fear``, ``joy``).  State transitions occur when
    ``tension`` exceeds ``0.7`` or ``emotion`` exceeds ``0.5``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        """Create a new agent.

        Parameters
        ----------
        name:
            Agent identifier.
        state:
            Initial ontological state.
        tension:
            Initial tension level.
        emotion:
            Intensity of the current emotion in range ``0-1``.
        emotion_type:
            Label of the dominant emotion (e.g. ``fear``, ``joy``).
        """
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            New emotion intensity in range ``0-1``.
        emotion_type:
            Optional new emotion label. If provided, ``emotion_type`` is
            updated as well.
        """
        self.emotion = value
        if emotion_type:
            self.emotion_type = emotion_type
        # Emotions feed into tension accumulation
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

        The response includes a short prefix reflecting the current emotion
        type.
        """
        emotion_prefix = {
            "anger": "Razburjeno pove: ",
            "fear": "Z zaskrbljenostjo pove: ",
            "joy": "Veselo pove: ",
        }.get(self.emotion_type, "")

        if self.state == "Ego":
            message = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            message = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            message = "Vse resnice so eno, medsebojno povezane."
        return f"{emotion_prefix}{message}"
