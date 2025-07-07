class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = {
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
            self.emotion_label["type"] = emotion_type
        self.emotion_label["value"] = value
        self.emotion_label["hidden"] = True
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def get_emotion_label(self) -> str:
        """Return the hidden emotion label."""
        return self.emotion_label["type"]

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
            Question posed to the agent (currently unused).
        reveal_emotion: bool, optional
            If True, include the hidden emotion label in the response.
        """
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if reveal_emotion and self.emotion_label["type"] != "neutral":
            return f"{base} Čutim {self.emotion_label['type']}."
        return base
