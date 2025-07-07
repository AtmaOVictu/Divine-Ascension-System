"""Agent module implementing a simple ontological state machine."""


class Agent:
    """Represent an ontological agent capable of transitioning states.

    The agent can reside in one of three states and keeps track of its current
    emotional intensity and type. State transitions are triggered when either
    the tension or emotion value crosses predefined thresholds.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_type: str | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, emotion_type: str, value: float) -> None:
        """Update emotion and adjust tension.

        Parameters
        ----------
        emotion_type:
            Type of the emotion (e.g. ``"fear"``, ``"joy"``, ``"anger"``).
        value:
            Intensity of the emotion in the ``0-1`` range.
        """

        self.emotion_type = emotion_type
        self.emotion = value
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
        """Return a philosophical answer influenced by the agent's state.

        The emotional state slightly colours the response when the intensity is
        high enough.
        """

        if self.state == "Ego":
            answer = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            answer = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            answer = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5 and self.emotion_type:
            prefix = {
                "anger": "V jezi trdim:",
                "fear": "V strahu priznavam:",
                "joy": "Z veseljem povem:",
            }.get(self.emotion_type, "")
            if prefix:
                answer = f"{prefix} {answer}"

        return answer
