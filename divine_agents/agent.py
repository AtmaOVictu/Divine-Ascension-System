"""Agent and sub-agent implementation with logging utilities."""

from __future__ import annotations

import time
from datetime import datetime


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.sub_agents: list[SubAgent] = []
        self.logs: list[str] = []
        self.log_file = f"{self.name}_log.txt"
        self.version = 1
        self.timestamp = time.time()

    # ------------------------------------------------------------------
    # Logging utilities
    # ------------------------------------------------------------------
    def log(self, message: str) -> None:
        """Log an action with a UTC timestamp to the log file."""
        ts = datetime.utcnow().isoformat()
        entry = f"{ts} - {message}"
        self.logs.append(entry)
        with open(self.log_file, "a", encoding="utf-8") as fh:
            fh.write(entry + "\n")
        self.timestamp = time.time()

    def sort_logs(self) -> list[str]:
        """Return logs sorted by timestamp."""
        return sorted(self.logs, key=lambda x: x.split(" - ")[0])

    def add_sub_agent(self, sub_agent: "SubAgent") -> None:
        """Attach a sub-agent and log the action."""
        self.sub_agents.append(sub_agent)
        self.log(f"Sub-agent {sub_agent.name} added")

    # ------------------------------------------------------------------
    # State management
    # ------------------------------------------------------------------
    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.log(f"Emotion updated to {value}")
        for sa in self.sub_agents:
            sa.log(f"Emotion updated to {value}")

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.log(f"Tension set to {value}")
        for sa in self.sub_agents:
            sa.log(f"Tension set to {value}")

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        previous = self.state
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        if self.state != previous:
            self.log(f"State transitioned to {self.state}")
            for sa in self.sub_agents:
                sa.log(f"State transitioned to {self.state}")
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
    def save_history(self) -> str:
        """Persist agent state history to disk."""
        filename = f"{self.name}_history_{self.version}.txt"
        with open(filename, "w", encoding="utf-8") as fh:
            fh.write(f"State History for {self.name}\n")
            for state in self.history:
                fh.write(state + "\n")
        return filename


class SubAgent:
    """A helper agent that logs its actions to the parent agent."""

    def __init__(self, name: str, associated_agent: Agent):
        self.name = name
        self.associated_agent = associated_agent
        self.logs: list[str] = []

    def log(self, message: str) -> None:
        ts = datetime.utcnow().isoformat()
        entry = f"{ts} - {message}"
        self.logs.append(entry)
        with open(self.associated_agent.log_file, "a", encoding="utf-8") as fh:
            fh.write(f"{self.name}: {entry}\n")
        self.associated_agent.timestamp = time.time()

    # Alias used in tests
    def log_action(self, message: str) -> None:
        self.log(message)

    def sort_logs(self) -> list[str]:
        return sorted(self.logs, key=lambda x: x.split(" - ")[0])
