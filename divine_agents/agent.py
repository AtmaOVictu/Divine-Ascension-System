from enum import Enum, auto


class Emotion(Enum):
    """Basic emotional types influencing agent tension."""

    NEUTRAL = auto()
    FEAR = auto()
    JOY = auto()
    ANGER = auto()


class Agent:
    """Ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0, emotion: float = 0.0, emotion_type: Emotion = Emotion.NEUTRAL):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: Emotion | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly.

        Parameters
        ----------
        value:
            New emotion intensity in the ``[0, 1]`` range.
        emotion_type:
            Optional ``Emotion`` type.  If provided, it replaces the current
            emotional label.
        """

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
        """Return a philosophical answer depending on state and emotion."""
        emotion_note = ""
        if self.emotion > 0.5:
            if self.emotion_type == Emotion.FEAR:
                emotion_note = " Občutim strah."
            elif self.emotion_type == Emotion.JOY:
                emotion_note = " Preveva me veselje."
            elif self.emotion_type == Emotion.ANGER:
                emotion_note = " Občutim jezo."

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        return f"{base}{emotion_note}"
