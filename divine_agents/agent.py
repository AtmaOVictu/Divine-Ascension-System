class Agent:
    """Represents an ontological agent capable of transitioning states.

    Each agent tracks a philosophical state (``Ego``, ``Jaz`` or ``Enotnost``)
    together with a current emotional intensity and type. State transitions
    occur once the agent's ``tension`` exceeds ``0.7`` or its ``emotion`` level
    is higher than ``0.5``.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_type: str = "neutral",
    ):
        """Create a new agent.

        Parameters
        ----------
        name:
            Identifier for the agent.
        state:
            Initial ontological state.
        tension:
            Initial tension level.
        emotion:
            Initial emotional intensity.
        emotion_type:
            Label describing the current emotion (e.g. ``fear`` or ``joy``).
        """
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def set_emotion(self, kind: str, intensity: float) -> None:
        """Set an emotion type and update intensity.

        Parameters
        ----------
        kind:
            Name of the emotion (e.g. ``fear``).
        intensity:
            Numeric intensity affecting tension.
        """
        self.emotion_type = kind
        self.update_emotion(intensity)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def emotion_label(self) -> str:
        """Return a textual label for the current emotion."""
        return self.emotion_type

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
        """Return a philosophical answer influenced by the agent's state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return f"({self.emotion_label()}) {base}"
