from .emotions import Emotion
from .karma import Karma


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: Emotion | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion_profile = emotion or Emotion()
        self.karma = Karma()
        self.history = [state]

    @property
    def emotion_level(self) -> float:
        """Return the highest intensity among emotional states."""
        return max(
            self.emotion_profile.joy,
            self.emotion_profile.anger,
            self.emotion_profile.fear,
            self.emotion_profile.sadness,
            self.emotion_profile.guilt,
            self.emotion_profile.hope,
            self.emotion_profile.pride,
            self.emotion_profile.despair,
        )

    def update_emotion(self, emotion: Emotion) -> None:
        """Set a new emotional profile and adjust tension."""
        self.emotion_profile = emotion
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
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
