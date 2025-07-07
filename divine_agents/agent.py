from enum import Enum


class Emotion(Enum):
    """Enumeration of basic emotions influencing tension."""

    FEAR = "fear"
    JOY = "joy"
    ANGER = "anger"
    NEUTRAL = "neutral"


class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", *, tension: float = 0.0, emotion_level: float = 0.0,
                 emotion_type: Emotion = Emotion.NEUTRAL):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_level = emotion_level
        self.emotion_type = emotion_type
        self.history = [state]

    def update_emotion(self, value: float, kind: Emotion | None = None) -> None:
        """Update emotion level and adjust tension.

        Parameters
        ----------
        value:
            New intensity of the emotion in the range ``0.0`` - ``1.0``.
        kind:
            Optional :class:`Emotion` describing the current emotion type.
        """

        self.emotion_level = value
        if kind is not None:
            self.emotion_type = kind

        # Influence tension based on emotion type
        multiplier = 1.0
        if self.emotion_type in (Emotion.FEAR, Emotion.ANGER):
            multiplier = 1.2
        elif self.emotion_type == Emotion.JOY:
            multiplier = 0.5
        self.tension += value * multiplier

    def update_tension(self, value: float) -> None:
        """Directly set the agent's tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if tension or emotion thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state and emotion."""
        prefix_map = {
            Emotion.FEAR: "Z zaskrbljenostjo, ",
            Emotion.JOY: "Veselo, ",
            Emotion.ANGER: "Jezen, ",
        }
        prefix = prefix_map.get(self.emotion_type, "")

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{prefix}{base}"
