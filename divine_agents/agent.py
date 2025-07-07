from __future__ import annotations
from datetime import datetime
from typing import List


class Agent:
    """Represents an ontological agent capable of transitioning states.

    Agents maintain an internal log with timestamps and can manage sub-agents
    that observe their actions. State transitions occur when either emotion or
    tension passes predefined thresholds.
    """

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history: List[str] = [state]
        self.sub_agents: List[Agent] = []
        self.logs: List[str] = []
        self.log_file = f"{self.name}.log"
        self.version = "1.0"
        self.timestamp = datetime.utcnow().timestamp()

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.log(f"Emotion updated to {value}")

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.log(f"Tension set to {value}")

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        previous_state = self.state
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        if self.state != previous_state:
            self.log(f"State transitioned to {self.state}")
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def log(self, message: str) -> None:
        """Write a timestamped message to the log."""
        now = datetime.utcnow()
        self.timestamp = now.timestamp()
        entry = f"{now.isoformat()} | {message}"
        self.logs.append(entry)
        with open(self.log_file, "a", encoding="utf-8") as fh:
            fh.write(entry + "\n")

    def add_sub_agent(self, sub_agent: "Agent") -> None:
        """Attach a sub-agent to this agent."""
        self.sub_agents.append(sub_agent)
        self.log(f"Sub-agent {sub_agent.name} added")

    def sort_logs(self) -> List[str]:
        """Return logs sorted chronologically."""
        return sorted(self.logs, key=lambda x: x.split(" | ")[0])

    def save_history(self) -> str:
        """Persist the state history to a file."""
        filename = f"{self.name}_history_{self.version}.txt"
        with open(filename, "w", encoding="utf-8") as fh:
            fh.write(f"State History for {self.name}\n")
            for state in self.history:
                fh.write(state + "\n")
        return filename
