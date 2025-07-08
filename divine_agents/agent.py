from typing import Iterable

from .emotion import Emotion
from .karma import Karma


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        # Extended emotional and karmic tracking
        self.emotion_state = Emotion()
        self.karma = Karma()

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        # Map simple emotion level to joy for karma updates
        self.emotion_state.joy = max(0.0, value)
        self.emotion_state.fear = max(0.0, -value)
        self.karma.update(self.emotion_state)

    def contagion(self, others: Iterable["Agent"], influence_factor: float = 0.2) -> None:
        """Spread emotions between agents, modifying this agent's emotion."""
        if not others:
            return
        avg = sum(a.emotion for a in others) / len(list(others))
        self.emotion += avg * influence_factor
        # Keep emotions within sensible bounds
        if self.emotion > 1:
            self.emotion = 1
        elif self.emotion < -1:
            self.emotion = -1
        self.karma.update(self.emotion_state, emotional_influence=avg * influence_factor)

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

    def recover(self) -> None:
        """Allow emotions to transition towards balance."""
        self.emotion_state.transition()
        self.karma.update(self.emotion_state)

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
