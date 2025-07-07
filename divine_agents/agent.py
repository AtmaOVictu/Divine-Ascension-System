class Agent:
    """Represents an ontological agent capable of transitioning states.

    Each agent keeps track of a simple emotional state and tension level. When
    tension exceeds ``0.7`` or emotion intensity surpasses ``0.5`` the agent
    will progress to the next ontological phase. The agent can be in one of the
    following states:

    ``Ego`` -> ``Jaz`` -> ``Enotnost``.
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
        """Update emotion intensity and type and adjust tension accordingly."""
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
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        emotion_part = ""
        if self.emotion_type == "fear":
            emotion_part = " Čutim strah."
        elif self.emotion_type == "joy":
            emotion_part = " Preveva me veselje."
        elif self.emotion_type == "anger":
            emotion_part = " Čutim jezo."

        return base + emotion_part
