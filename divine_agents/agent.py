class Agent:
    """Represents an ontological agent capable of transitioning states.

    Each agent holds an ontological ``state`` (``Ego`` -> ``Jaz`` ->
    ``Enotnost``) together with a current ``emotion`` intensity and a
    textual ``emotion_type`` (e.g. ``fear``, ``joy``).  When the agent's
    tension or emotion exceeds predefined thresholds it will transition to
    the next state.  The agent is also able to respond to philosophical
    questions depending on its current state and emotion.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str | None = None):
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
            New emotion intensity.
        emotion_type:
            Optional textual description of the emotion (e.g. ``fear`` or
            ``joy``).
        """

        self.emotion = value
        if emotion_type is not None:
            self.emotion_type = emotion_type
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

        The text of the response also subtly reflects the agent's current
        emotional state if one is set.
        """

        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        if self.emotion_type:
            return f"{base} (čutim {self.emotion_type})"
        return base
