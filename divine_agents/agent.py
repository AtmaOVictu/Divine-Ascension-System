class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        # hidden metadata about the current emotion
        self._emotion_label = {
            "type": emotion_type,
            "value": emotion,
            "hidden": True,
        }
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value: float
            New emotion intensity.
        emotion_type: str | None
            Optional label of the emotion (e.g. 'strah', 'veselje').
        """
        self.emotion = value
        if emotion_type is not None:
            self.emotion_type = emotion_type
        self.tension += value
        self._emotion_label = {
            "type": self.emotion_type,
            "value": self.emotion,
            "hidden": True,
        }

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

    def respond(self, question: str, reveal_emotion: bool = False) -> str:
        """Return a philosophical answer depending on the current state.

        Parameters
        ----------
        question: str
            Prompt for the agent. Currently unused but kept for extensibility.
        reveal_emotion: bool, optional
            If True, include the current emotion label in the response.
        """
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if reveal_emotion and self.emotion_type != "neutral":
            return base + f" Čustvo: {self.emotion_type}."

        return base

    def get_emotion_label(self) -> dict:
        """Return the hidden emotion label metadata."""
        return self._emotion_label.copy()
