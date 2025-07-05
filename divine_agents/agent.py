from .emotion import EmotionTransformer


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float, *, transform: bool = True, k: float = 1.0) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value: float
            New raw emotion value in the range [-1, 1].
        transform: bool, optional
            When ``True``, apply a sigmoid based transformation so that
            negative emotions can mutate into the positive spectrum and
            vice-versa.
        k: float, optional
            Controls the steepness of the sigmoid transformation.
        """
        self.emotion = value
        if transform:
            transformer = EmotionTransformer(self.emotion, k)
            self.emotion = transformer.get_transformed_emotion()
        self.tension += abs(self.emotion)

    def transform_emotion(self, k: float = 1.0) -> float:
        """Transform the current emotion using :class:`EmotionTransformer`."""
        transformer = EmotionTransformer(self.emotion, k)
        self.emotion = transformer.get_transformed_emotion()
        return self.emotion

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
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
