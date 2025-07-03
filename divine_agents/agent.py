class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(
        self,
        *,
        tension: float | None = None,
        emotion: float | None = None,
        tension_threshold: float = 0.7,
        emotion_threshold: float = 0.5,
    ) -> str:
        """Perform state transition if thresholds are exceeded.

        Parameters
        ----------
        tension:
            Optional tension value to set before evaluating the transition.
        emotion:
            Optional emotion value to set before evaluating the transition.
        tension_threshold:
            Threshold for tension required to trigger a transition.
        emotion_threshold:
            Threshold for emotion required to trigger a transition.
        """
        if tension is not None:
            self.update_tension(tension)
        if emotion is not None:
            self.update_emotion(emotion)

        if self.tension > tension_threshold or self.emotion > emotion_threshold:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
