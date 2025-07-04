class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent stores a current ontological ``state`` and can move from
    ``Ego`` -> ``Jaz`` -> ``Enotnost`` when either ``tension`` or
    ``emotion`` exceeds predefined thresholds.  Each agent also tracks the
    name of the emotion currently influencing it so that dialogue responses
    can reflect the agent's mood.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_name: str = "neutral",
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, value: float, name: str = "neutral") -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            New emotional intensity in range ``0.0`` - ``1.0``.
        name:
            Optional descriptive name of the emotion (``fear``, ``anger``,
            ``joy`` ...).  This information is used when composing dialogue.
        """
        self.emotion = value
        self.emotion_name = name
        # Emotions increase overall tension inside the agent
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
        """Return a philosophical answer depending on the current state."""
        prefix = f"V \u010dustvu {self.emotion_name} pravim: "
        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z na\u0161imi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."
