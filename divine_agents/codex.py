from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Tuple

from .agent import Agent


@dataclass
class Codex:
    """Command processor that validates commands and orchestrates agent states."""

    agent: Agent
    allowed_commands: Tuple[str, ...] = ("move", "reset", "update")
    history: List[Tuple[str, str, str]] = field(default_factory=list)
    error_log: List[str] = field(default_factory=list)

    def execute(self, command: str, **kwargs) -> str:
        """Execute a command on the underlying agent."""
        if command not in self.allowed_commands:
            return self.handle_error(f"Invalid Command: {command}")

        prev_state = self.agent.state
        if command == "move":
            new_state = self.agent.transition()
        elif command == "reset":
            self.agent.state = "Ego"
            self.agent.tension = 0.0
            self.agent.emotion = 0.0
            new_state = self.agent.state
        elif command == "update":
            if "emotion" in kwargs:
                self.agent.update_emotion(kwargs["emotion"])
            if "tension" in kwargs:
                self.agent.update_tension(kwargs["tension"])
            new_state = self.agent.state
        else:  # pragma: no cover - should not happen
            return self.handle_error(f"Unhandled Command: {command}")

        self.history.append((prev_state, command, new_state))
        return new_state

    def handle_error(self, message: str) -> str:
        """Record an error and return an error message."""
        self.error_log.append(message)
        return f"Error: {message}"

    def get_history(self) -> List[Tuple[str, str, str]]:
        """Return command execution history."""
        return self.history

    def get_error_log(self) -> List[str]:
        """Return a list of recorded errors."""
        return self.error_log
