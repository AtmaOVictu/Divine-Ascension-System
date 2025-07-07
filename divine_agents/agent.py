"""Ontological agents capable of transitioning philosophical states."""

from __future__ import annotations

import os
import time
from typing import List


class SubAgent:
    """Lightweight helper agent that logs actions taken during transitions."""

    def __init__(self, name: str, associated_agent: "Agent") -> None:
        self.name = name
        self.associated_agent = associated_agent
        self.logs: List[str] = []

    def log_action(self, message: str) -> None:
        """Log an action with a timestamp."""
        entry = f"{time.time()}::{message}"
        self.logs.append(entry)

    def sort_logs(self) -> List[str]:
        """Return logs sorted by timestamp."""
        return sorted(self.logs, key=lambda line: float(line.split("::", 1)[0]))


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.sub_agents: List[SubAgent] = []
        self.log_file = f"{self.name}_log.txt"
        self.version = 1

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.log(f"Emotion updated to {value}")

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.log(f"Tension updated to {value}")

    def add_sub_agent(self, sub_agent: SubAgent) -> None:
        """Attach a sub-agent to this agent."""
        self.sub_agents.append(sub_agent)
        self.log(f"Sub-agent {sub_agent.name} added")

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            self.log(f"State transitioned to {self.state}")
            for sa in self.sub_agents:
                sa.log_action(f"State transitioned to {self.state}")
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            reply = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            reply = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            reply = "Vse resnice so eno, medsebojno povezane."
        self.log(f"Responded: {reply}")
        return reply

    def log(self, message: str) -> None:
        """Append a timestamped message to the agent's log file."""
        entry = f"{time.time()}::{message}\n"
        with open(self.log_file, "a", encoding="utf-8") as fh:
            fh.write(entry)

    def save_history(self) -> None:
        """Persist the agent's state history to a file."""
        filename = f"{self.name}_history_{self.version}.txt"
        with open(filename, "w", encoding="utf-8") as fh:
            fh.write(f"State History for {self.name}\n")
            for state in self.history:
                fh.write(f"{state}\n")
        self.version += 1
