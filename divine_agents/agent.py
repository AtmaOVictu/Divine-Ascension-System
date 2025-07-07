class Agent:
    """Ontological agent capable of transitioning states based on tension and emotion."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, mood: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.mood = mood
        self.history = [state]

    def update_emotion(self, value: float, mood: str = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value: float
            Intensity of the emotion.
        mood: str, optional
            Label describing the current emotion (e.g. 'fear', 'joy').
        """
        self.emotion = value
        if mood is not None:
            self.mood = mood
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition when tension or emotion exceed thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state and mood."""

        prefix = ""
        if self.mood == "anger":
            prefix = "(jeza) "
        elif self.mood == "fear":
            prefix = "(strah) "
        elif self.mood == "joy":
            prefix = "(veselje) "

        if self.state == "Ego":
            answer = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            answer = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            answer = "Vse resnice so eno, medsebojno povezane."
        return prefix + answer
