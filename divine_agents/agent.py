class Agent:
    """Represents an ontological agent capable of transitioning states.

    The agent holds an ontological ``state`` (``Ego`` → ``Jaz`` → ``Enotnost``),
    a numeric ``tension`` level and an ``emotion`` intensity.  Additionally an
    ``emotion_label`` describes the qualitative feeling (e.g. ``fear`` or
    ``joy``).  When either the ``tension`` exceeds ``0.7`` or the ``emotion``
    intensity exceeds ``0.5`` a state transition may occur.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_label: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_label = emotion_label
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def set_emotion(self, label: str, intensity: float) -> None:
        """Set both the qualitative emotion label and its intensity."""
        self.emotion_label = label
        self.update_emotion(intensity)

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

        The returned statement is influenced by the current ``emotion_label``
        to showcase how feelings affect the discourse.
        """
        prefix = ""
        if self.emotion_label == "fear":
            prefix = "S strahom, "
        elif self.emotion_label == "joy":
            prefix = "Z veseljem, "
        elif self.emotion_label == "anger":
            prefix = "Z jezo, "

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return prefix + base
