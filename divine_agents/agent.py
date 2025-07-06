class Agent:
    """Represents an ontological agent capable of transitioning states.

    Parameters
    ----------
    name:
        Identifier of the agent.
    state:
        Initial ontological state (``"Ego"``, ``"Jaz"``, or ``"Enotnost"``).
    tension:
        Initial tension level which may trigger state transitions.
    emotion:
        Initial intensity of the current emotion.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = ""
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def feel(self, emotion_name: str, intensity: float) -> None:
        """Record the current emotion and modify tension.

        Parameters
        ----------
        emotion_name:
            Descriptive name of the emotion (e.g., ``"jeza"``, ``"strah"``).
        intensity:
            Value between 0 and 1 representing how strong the emotion is.
        """
        self.emotion_name = emotion_name
        self.update_emotion(intensity)

    def update_tension(self, value: float) -> None:
        """Directly set tension level.

        Parameters
        ----------
        value:
            New tension value between 0 and 1.
        """
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded.

        A transition occurs when ``tension`` is greater than ``0.7`` or
        ``emotion`` is greater than ``0.5``. ``Ego`` moves to ``Jaz`` and
        ``Jaz`` moves to ``Enotnost``.
        """
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
