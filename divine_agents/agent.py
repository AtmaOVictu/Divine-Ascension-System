class Agent:
    """Represent an ontological agent capable of transitioning ontological
    states based on emotion and tension levels.

    The agent moves from ``Ego`` -> ``Jaz`` -> ``Enotnost`` once either the
    tension or emotion thresholds are exceeded.  Emotions also carry a label
    (e.g. ``"jeza"`` for anger) used in responses.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_type: str | None = None,
    ) -> None:
        """Initialise the agent.

        Parameters
        ----------
        name:
            Display name of the agent.
        state:
            Current ontological state.
        tension:
            Current tension level.
        emotion:
            Current emotion intensity.
        emotion_type:
            Optional description of the current emotion (e.g. ``"strah"``).
        """

        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type or "nevtralno"
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update the emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            New emotion intensity.
        emotion_type:
            Optional label describing the emotion.
        """

        self.emotion = value
        if emotion_type is not None:
            self.emotion_type = emotion_type
        # Emotions contribute directly to tension growth
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""

        self.tension = value

    def transition(self) -> str:
        """Perform a state transition when thresholds are exceeded."""

        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer reflecting the current state and
        emotional stance."""

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return f"{base} (Čutim {self.emotion_type}.)"
