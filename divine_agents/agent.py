from enum import Enum


class EmotionType(Enum):
    """Enumerates supported emotional expressions."""

    NEUTRAL = "neutral"
    FEAR = "fear"
    JOY = "joy"
    ANGER = "anger"


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotion_type: EmotionType = EmotionType.NEUTRAL,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: EmotionType | None = None) -> None:
        """Update emotion intensity and optionally its type.

        Parameters
        ----------
        value:
            Intensity of the current emotion.
        emotion_type:
            Optional new emotional expression.
        """

        self.emotion = value
        self.tension += value
        if emotion_type is not None:
            self.emotion_type = emotion_type

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

        emotion_appendix = {
            EmotionType.FEAR: "Čutim strah, kar me vodi k dvomom.",
            EmotionType.JOY: "Občutim veselje, kar krepi moj pogled.",
            EmotionType.ANGER: "Jeza me razburja, a verjamem v svoje besede.",
            EmotionType.NEUTRAL: "",
        }

        appendix = emotion_appendix.get(self.emotion_type, "")
        return f"{base} {appendix}".strip()
