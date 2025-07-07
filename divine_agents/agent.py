"""Core agent logic for the ontological framework."""
from __future__ import annotations

import time
from typing import List


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.sub_agents: List["SubAgent"] = []
        self.timestamp = time.time()
        self.version = self._generate_version()

    def _generate_version(self) -> str:
        """Generate a version identifier based on creation time."""
        return time.strftime("%Y%m%d%H%M%S", time.gmtime(self.timestamp))

    def add_sub_agent(self, sub_agent: "SubAgent") -> None:
        """Attach a helper sub-agent."""
        self.sub_agents.append(sub_agent)

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
        self.timestamp = time.time()
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            response = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            response = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            response = "Vse resnice so eno, medsebojno povezane."

        for helper in self.sub_agents:
            helper.log_action(f"Agent {self.name} responded with: {response}")

        return response


# Forward declaration for type checking
from .manager import SubAgent  # noqa: E402  (import at end to avoid circular ref)
