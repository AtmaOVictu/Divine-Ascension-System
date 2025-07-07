class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Display name of the agent.
    state:
        Initial ontological state. One of ``Ego``, ``Jaz`` or ``Enotnost``.
    tension:
        Initial tension level.
    emotion:
        Initial emotion intensity.
    emotion_name:
        Optional human readable name of the current emotion.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_name: str | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name or "brezčutnost"
        self.history = [state]

    def update_emotion(self, value: float, name: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            New emotion intensity.
        name:
            Optional label for the emotion (e.g., ``jeza``, ``strah``).
        """
        self.emotion = value
        if name is not None:
            self.emotion_name = name
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

        The emotional label is included in the response to highlight how the
        agent currently feels about the discussion.
        """
        prefix = f"Občutim {self.emotion_name}; "

        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."

        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."

        return prefix + "Vse resnice so eno, medsebojno povezane."
