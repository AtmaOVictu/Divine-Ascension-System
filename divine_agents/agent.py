class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

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
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    # New functionality for saving and loading agent state
    def to_dict(self) -> dict:
        """Serialize the agent state to a dictionary."""
        return {
            "name": self.name,
            "state": self.state,
            "tension": self.tension,
            "emotion": self.emotion,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Agent":
        """Instantiate an Agent from a serialized dictionary."""
        return cls(
            data.get("name", "Unnamed"),
            state=data.get("state", "Ego"),
            tension=data.get("tension", 0.0),
            emotion=data.get("emotion", 0.0),
        )

    def save(self, path: str) -> None:
        """Save the agent state to a JSON file."""
        import json

        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f)

    @classmethod
    def load(cls, path: str) -> "Agent":
        """Load an Agent instance from a JSON file."""
        import json

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls.from_dict(data)
