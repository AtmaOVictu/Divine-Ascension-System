from typing import Dict

from .emotions import Emotion


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        # store emotions by name
        self.emotions: Dict[str, Emotion] = {}
        self.history = [state]

    # ------------------------------------------------------------------
    # Emotion and tension handling
    # ------------------------------------------------------------------
    def set_emotion(self, name: str, intensity: float) -> None:
        """Set an emotion and adjust tension accordingly."""
        self.emotions[name] = Emotion(name, intensity)
        # tension increases with new emotion intensity
        self.tension += intensity

    @property
    def max_emotion_intensity(self) -> float:
        return max((e.intensity for e in self.emotions.values()), default=0.0)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    # ------------------------------------------------------------------
    # State transitions and responses
    # ------------------------------------------------------------------
    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.max_emotion_intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def dominant_emotion(self) -> str:
        if not self.emotions:
            return ""
        # emotion with highest intensity
        return max(self.emotions.values(), key=lambda e: e.intensity).name

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state and emotion."""
        if self.state == "Ego":
            message = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            message = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            message = "Vse resnice so eno, medsebojno povezane."

        emotion = self.dominant_emotion()
        if emotion:
            if emotion == "fear":
                message += " Čutim strah."
            elif emotion == "joy":
                message += " Preveva me veselje."
            elif emotion == "anger":
                message += " Preveva me jeza."
        return message
