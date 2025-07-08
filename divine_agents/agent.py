from typing import Optional

from .emotion import Emotion
from .karma import Karma


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion_level: float = 0.0, emotion: Optional[Emotion] = None,
                 karma: Optional[Karma] = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_level = emotion_level
        self.emotion = emotion if emotion is not None else Emotion()
        self.karma = karma if karma is not None else Karma()
        self.history = [state]

    def update_emotion(self, **kwargs: float) -> None:
        """Update emotional values and adjust tension accordingly."""
        for key, val in kwargs.items():
            if hasattr(self.emotion, key):
                setattr(self.emotion, key, val)
        self.emotion_level = self.emotion.intensity()
        self.tension += self.emotion_level

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.karma.update(self.emotion)
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        emotion_suffix = ''
        if self.emotion.anger > 0.5:
            emotion_suffix = ' (jezen)'
        elif self.emotion.joy > 0.5:
            emotion_suffix = ' (vesel)'
        elif self.emotion.fear > 0.5:
            emotion_suffix = ' (prestrašen)'

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return base + emotion_suffix
