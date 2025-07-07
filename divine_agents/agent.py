import time
from typing import List


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    # Default emotional weights that contribute to tension
    EMOTIONS = {
        "fear": 0.3,
        "joy": 0.7,
        "anger": 0.5,
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: str = "joy"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history: List[str] = [state]
        self.logs: List[str] = []
        self.timestamp = time.time()

    def log(self, message: str) -> None:
        """Store a timestamped log message for self-awareness."""
        timestamp_str = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(self.timestamp))
        entry = f"{timestamp_str} - {self.name}: {message}"
        self.logs.append(entry)

    def update_emotion(self, emotion: str) -> None:
        """Update the agent's emotion and modify tension."""
        self.emotion = emotion
        self.tension += self.EMOTIONS.get(emotion, 0.0)
        self.log(f"Emotion updated to {emotion}")

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.log(f"Tension updated to {value}")

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.EMOTIONS.get(self.emotion, 0.0) > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            self.log(f"Transitioned to {self.state}")
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            answer = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            answer = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            answer = "Vse resnice so eno, medsebojno povezane."
        self.log(f"Responded with: {answer} (emotion: {self.emotion})")
        return answer
