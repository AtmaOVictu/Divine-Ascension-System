import time
from typing import List


class Agent:
    """Represents an ontological agent with emotional self-awareness."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTIONS = {
        "fear": 0.3,
        "joy": 0.7,
        "anger": 0.5,
    }

    def __init__(self, name: str, state: str = "Ego", emotion: str = "joy", tension: float = 0.0):
        self.name = name
        self.state = state
        self.emotion = emotion
        self.tension = tension
        self.history: List[str] = [state]
        self.logs: List[str] = []
        self.timestamp = time.time()

    def log(self, message: str) -> None:
        """Record an action with timestamp for self-awareness."""
        timestamp_str = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(self.timestamp))
        entry = f"{timestamp_str} - {self.name}: {message}"
        self.logs.append(entry)

    def update_emotion(self, emotion: str) -> None:
        """Update the agent's emotion and adjust tension accordingly."""
        self.emotion = emotion
        self.tension += self.EMOTIONS.get(emotion, 0.0)
        self.timestamp = time.time()
        self.log(f"emotion updated to {self.emotion}")

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.timestamp = time.time()
        self.log(f"tension set to {self.tension}")

    def transition(self) -> str:
        """Perform state transition if emotion or tension thresholds are met."""
        emotion_value = self.EMOTIONS.get(self.emotion, 0.0)
        if self.tension > 0.7 or emotion_value > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            self.log(f"transitioned to {self.state}")
        self.history.append(self.state)
        self.timestamp = time.time()
        return self.state

    def respond(self, question: str) -> str:
        """Generate a philosophical response influenced by the current state."""
        if self.state == "Ego":
            answer = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            answer = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            answer = "Vse resnice so eno, medsebojno povezane."
        response = f"{answer} Čustvo: {self.emotion}."
        self.log(f"responded: {response}")
        return response
