"""Core agent logic handling states, emotions and transitions."""

from typing import List


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, mood: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.mood = mood
        self.history: List[str] = [state]

    def update_emotion(self, mood: str, value: float) -> None:
        """Update emotion intensity and adjust tension based on mood."""
        self.mood = mood
        self.emotion = value
        if mood == "anger":
            self.tension += value
        elif mood == "joy":
            self.tension -= value / 2
        elif mood == "fear":
            self.tension += 1.5 * value
        else:
            self.tension += value / 2
        if self.tension < 0:
            self.tension = 0.0

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
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }
        return base.get(self.state, "") + self._determine_tone()

    def _determine_tone(self) -> str:
        """Determine textual tone suffix based on mood."""
        tone_mapping = {
            "anger": " (spoken with anger)",
            "fear": " (spoken with fear)",
            "joy": " (spoken with joy)",
            "neutral": "",
        }
        return tone_mapping.get(self.mood, "")
