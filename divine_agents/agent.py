import json
from typing import Any, Dict, List


class Agent:
    """Represents an ontological agent capable of transitioning states.

    Agents can persist their current configuration and history to a JSON file
    so that conversations can be resumed later. The ``save`` and ``load``
    methods provide a simple interface for this functionality.
    """

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

    # ------------------------------------------------------------------
    # Persistence utilities
    # ------------------------------------------------------------------
    def to_dict(self) -> Dict[str, Any]:
        """Return a serialisable representation of the agent."""
        return {
            "name": self.name,
            "state": self.state,
            "tension": self.tension,
            "emotion": self.emotion,
            "history": self.history,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Agent":
        """Construct an ``Agent`` instance from a dictionary."""
        agent = cls(
            data.get("name", "Unnamed"),
            state=data.get("state", "Ego"),
            tension=data.get("tension", 0.0),
            emotion=data.get("emotion", 0.0),
        )
        agent.history = data.get("history", [agent.state])
        return agent

    def save(self, path: str) -> None:
        """Persist the agent's data to ``path`` in JSON format."""
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f)

    @classmethod
    def load(cls, path: str) -> "Agent":
        """Load agent data from ``path`` and return a new ``Agent`` instance."""
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls.from_dict(data)
