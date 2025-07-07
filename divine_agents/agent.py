import time


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    EMOTIONS = {
        "fear": 0.3,
        "joy": 0.7,
        "anger": 0.5,
    }

    def __init__(self, name: str, state: str = "Ego", emotion: str = "joy"):
        self.name = name
        self.state = state
        self.emotion = emotion
        self.tension = 0.0
        self.history = [state]
        self.timestamp = time.time()

    def update_emotion(self, emotion: str) -> None:
        """Update the agent's emotion and adjust tension."""
        self.emotion = emotion
        self.tension += self.EMOTIONS.get(emotion, 0.0)
        self.timestamp = time.time()
        self.log(f"Self-awareness: {self.name}'s emotion updated to {self.emotion}")

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.timestamp = time.time()

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        emotion_value = self.EMOTIONS.get(self.emotion, 0.0)
        if self.tension > 0.7 or emotion_value > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            elif self.state == "Enotnost":
                self.state = "Ego"
        self.history.append(self.state)
        self.timestamp = time.time()
        self.log(f"Self-awareness: {self.name} transitioned to {self.state}")
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        response = f"{base} Emotion: {self.emotion}."
        self.log(
            f"Self-awareness: {self.name} responded with emotional tone: {response}"
        )
        return response

    def log(self, message: str) -> None:
        """Log agent actions with timestamp."""
        timestamp_str = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(self.timestamp))
        print(f"{timestamp_str} - {self.name}: {message}")
