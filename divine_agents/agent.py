class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Human readable name of the agent.
    state:
        Starting ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension:
        Current level of tension. Values greater than ``0.7`` may trigger
        a state transition.
    emotion:
        Intensity of the current emotion. Values greater than ``0.5`` may
        also trigger a state transition.
    emotion_name:
        Description of the emotion (e.g. ``fear``, ``joy`` or ``anger``).
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_name: str | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name or ""
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def set_emotion(self, name: str, intensity: float) -> None:
        """Set emotion name and intensity."""
        self.emotion_name = name
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
        """Return a philosophical answer depending on the current state."""
        prefix = ""
        if self.emotion_name == "fear":
            prefix = "V strahu povem: "
        elif self.emotion_name == "joy":
            prefix = "Z veseljem povem: "
        elif self.emotion_name == "anger":
            prefix = "Z jezo poudarjam: "

        if self.state == "Ego":
            statement = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            statement = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            statement = "Vse resnice so eno, medsebojno povezane."

        return prefix + statement
