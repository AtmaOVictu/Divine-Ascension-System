class Agent:
    """Ontological agent capable of changing philosophical states.

    Parameters
    ----------
    name:
        Human readable name of the agent.
    state:
        Initial ontological state. One of ``"Ego"``, ``"Jaz"`` or
        ``"Enotnost"``.
    tension:
        Initial internal tension.
    emotion:
        Initial emotion intensity.
    emotion_type:
        Type of emotion (e.g. ``"fear"``, ``"joy"`` or ``"anger"``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0, emotion: float = 0.0, emotion_type: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, emotion_type: str, value: float) -> None:
        """Update emotion intensity and adjust tension.

        Fear and anger increase tension more than other emotions.
        """
        self.emotion_type = emotion_type
        self.emotion = value
        if emotion_type in {"fear", "anger"}:
            self.tension += value
        else:
            self.tension += value / 2

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition when thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return an answer influenced by the state and current emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_type == "fear":
            mood = "z zaskrbljenostjo"
        elif self.emotion_type == "anger":
            mood = "z jezo"
        elif self.emotion_type == "joy":
            mood = "z veseljem"
        else:
            mood = "mirno"

        return f"{base} Odgovarjam {mood}."
