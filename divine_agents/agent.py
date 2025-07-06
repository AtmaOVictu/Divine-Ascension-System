class Agent:
    """Represents an ontological agent capable of transitioning states.

    An agent keeps track of its ontological state (``Ego`` | ``Jaz`` | ``Enotnost``)
    alongside the current emotional intensity and type.  State transitions occur
    when either ``tension`` exceeds ``0.7`` or ``emotion`` exceeds ``0.5``.  The
    agent also formulates responses based on its state and emotional context.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_type: str = "neutral",
    ) -> None:
        """Create a new agent.

        Parameters
        ----------
        name:
            Agent identifier.
        state:
            Initial ontological state.
        tension:
            Starting tension value.
        emotion:
            Starting emotion intensity ``0-1``.
        emotion_type:
            Descriptor of the emotion (e.g. ``fear``, ``anger``, ``joy``).
        """

        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and optionally change emotion type.

        Parameters
        ----------
        value:
            New emotion intensity ``0-1``.
        emotion_type:
            If provided, update the ``emotion_type`` attribute as well.
        """

        self.emotion = value
        if emotion_type is not None:
            self.emotion_type = emotion_type
        # emotion contributes to tension build-up
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded.

        Returns the new state after the transition check.  The state will move
        ``Ego -> Jaz`` or ``Jaz -> Enotnost`` when ``tension`` is greater than
        ``0.7`` or ``emotion`` is greater than ``0.5``.
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

        prefixes = {
            "fear": "V strahu",
            "anger": "Z jezo",
            "joy": "Z veseljem",
        }
        prefix = prefixes.get(self.emotion_type, "Mirno")

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return f"{prefix}, {base}"
