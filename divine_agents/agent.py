class Agent:
    """Represents an ontological agent capable of transitioning states.

    Attributes
    ----------
    name: str
        Identifier of the agent.
    state: str
        Current ontological state. One of ``"Ego"``, ``"Jaz"`` or ``"Enotnost"``.
    tension: float
        Accumulated tension value. If it exceeds the threshold it may trigger a
        state transition.
    emotion: float
        Current intensity of the emotional state.
    emotion_name: str
        Name of the emotion (e.g. ``"fear"``, ``"joy"``, ``"anger"``).
    history: list[str]
        Keeps track of states the agent has been in.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_name: str = ""):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, value: float, name: str | None = None) -> None:
        """Update emotion intensity and optionally its name.

        Updating the emotion also increases the agent's tension which may
        trigger a state change on the next :py:meth:`transition` call.
        """
        self.emotion = value
        if name is not None:
            self.emotion_name = name
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
        """Return a philosophical answer depending on the current state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_name == "fear":
            emotion_part = " Čutim strah."
        elif self.emotion_name == "joy":
            emotion_part = " Preveva me veselje."
        elif self.emotion_name == "anger":
            emotion_part = " Občutim jezo."
        else:
            emotion_part = ""

        return base + emotion_part
