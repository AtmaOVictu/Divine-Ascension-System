class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTIONS = ("neutral", "fear", "joy", "anger")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_name: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, value: float, emotion_name: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            Intensity of the emotion in the range ``0.0`` - ``1.0``.
        emotion_name:
            Optional name of the emotion influencing the agent.
        """
        self.emotion = value
        self.tension += value
        if emotion_name is not None:
            self.emotion_name = emotion_name

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
        """Return a philosophical answer depending on the current state and emotion."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        emotion_note = {
            "fear": "Strah me navdaja.",
            "joy": "Občutim veselje.",
            "anger": "Jeza me prevzema.",
        }.get(self.emotion_name, "")

        return f"{base} {emotion_note}".strip()
