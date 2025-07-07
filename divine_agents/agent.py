class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name: str
        Agent identifier.
    state: str, optional
        Initial ontological state.
    tension: float, optional
        Initial tension level.
    emotion_intensity: float, optional
        Intensity of the current emotion.
    emotion: str, optional
        Name of the current emotion.
    stable_axis: str, optional
        State representing the stable axis to which the agent returns.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion_intensity: float = 0.0,
        emotion: str = "neutral",
        stable_axis: str = "Enotnost",
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_intensity = emotion_intensity
        self.emotion = emotion
        self.stable_axis = stable_axis
        self.history = [state]

    def update_emotion(self, value: float, name: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value: float
            Intensity of the emotion.
        name: str | None, optional
            Name of the emotion. If provided, updates the current emotion.
        """

        if name is not None:
            self.emotion = name
        self.emotion_intensity = value
        self.tension += value
        # Fear may cause immediate return to stable axis
        if self.emotion == "fear":
            self.state = self.stable_axis

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded.

        Returns the new state.
        """
        if self.tension > 0.7 or self.emotion_intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"

        if self.state != self.stable_axis:
            self.history.append(f"Agent {self.name} is in a transitional state: {self.state}")
        else:
            self.history.append(f"Agent {self.name} has returned to stable axis: {self.state}")

        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.state != self.stable_axis:
            base += f" Trenutno prehajam iz {self.stable_axis}."

        return base
