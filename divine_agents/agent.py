"""Core logic for agents within the ontological framework."""

from typing import Dict


EMOTION_IMPACT: Dict[str, float] = {
    "fear": 0.6,
    "joy": 0.2,
    "anger": 0.7,
    "neutral": 0.0,
}


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, emotion: str) -> None:
        """Set emotion and adjust tension based on predefined impact."""
        self.emotion = emotion
        self.tension += EMOTION_IMPACT.get(emotion, 0.0)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        emotion_level = EMOTION_IMPACT.get(self.emotion, 0.0)
        if self.tension > 0.7 or emotion_level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current emotion."""
        prefix = {
            "fear": "S strahom odgovarjam:",
            "joy": "Z veseljem odgovarjam:",
            "anger": "Z jezo odgovarjam:",
            "neutral": "",
        }.get(self.emotion, "")

        if self.state == "Ego":
            answer = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            answer = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            answer = "Vse resnice so eno, medsebojno povezane."

        if prefix:
            return f"{prefix} {answer}"
        return answer
