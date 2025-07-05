from .utils import logistic_function


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_name: str | None = None) -> None:
        """Create a new agent.

        Parameters
        ----------
        name:
            Agent identifier.
        state:
            Ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
        tension:
            Current tension level ranging between 0 and 1.
        emotion:
            Numeric intensity of the current emotion.
        emotion_name:
            Name of the emotion the agent is experiencing.
        """
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_name = emotion_name or "neutral"
        self.history = [state]

    def update_emotion(self, value: float, emotion_name: str | None = None) -> None:
        """Update emotion intensity and adjust tension.

        Parameters
        ----------
        value:
            Numeric intensity of the emotion.
        emotion_name:
            Optional name describing the emotion (e.g. ``"fear"``).
        """
        self.emotion = value
        if emotion_name:
            self.emotion_name = emotion_name
        # Tension rises according to a logistic curve and is clamped to 1.0
        self.tension = min(1.0, logistic_function(self.tension + value))

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
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            answer = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            answer = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            answer = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_name != "neutral":
            answer += f" Občutim {self.emotion_name}."
        return answer
