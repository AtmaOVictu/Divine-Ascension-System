from .emotion import EmotionTransformer


class Agent:
    """Ontological agent capable of transitioning states based on emotion and tension."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Emotion values lie in ``[-1, 1]`` where the sign represents polarity.
        The raw value is transformed toward its polarity using
        :class:`EmotionTransformer` and the absolute intensity contributes to
        agent tension.
        """
        transformer = EmotionTransformer(value)
        self.emotion = transformer.get_transformed_emotion()
        self.tension += abs(self.emotion)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, value)

    def transition(self) -> str:
        """Perform state transition when tension or emotion cross thresholds."""
        intensity = abs(self.emotion)
        if self.tension > 0.7 or intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            return base + " Čutim veselje ob tem spoznanju."
        if self.emotion < -0.5:
            return base + " Čutim žalost ob tem razmisleku."
        return base
