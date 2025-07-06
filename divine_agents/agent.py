from enum import Enum


class EmotionType(Enum):
    """Enumeration of supported emotional states."""

    NEUTRAL = "neutral"
    FEAR = "fear"
    JOY = "joy"
    ANGER = "anger"
    SORROW = "sorrow"


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
        self.tension = float(tension)
        self.emotion = float(emotion)
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, emotion_type: EmotionType) -> None:
        """Update emotion intensity, type and adjust tension accordingly."""
        self.emotion = float(value)
        self.emotion_type = emotion_type
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = float(value)

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
        """Return a philosophical answer influenced by state and emotion."""
        base = ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        emotion_phrases = {
            EmotionType.FEAR: "Občutim strah.",
            EmotionType.JOY: "Preveva me veselje.",
            EmotionType.ANGER: "Začutim jezo.",
            EmotionType.SORROW: "Preveva me žalost.",
            EmotionType.NEUTRAL: "",
        }
        phrase = emotion_phrases.get(self.emotion_type, "")
        return f"{base} {phrase}".strip()
