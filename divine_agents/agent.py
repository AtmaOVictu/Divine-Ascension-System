from __future__ import annotations

from typing import List

from .sub_agent import SubAgent


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

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self._notify_sub_agents("Emotion updated")

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self._notify_sub_agents("Tension updated")

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        self._notify_sub_agents(f"State transitioned to {self.state}")
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            response = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            response = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            response = "Vse resnice so eno, medsebojno povezane."
        self._notify_sub_agents("Response generated")
        return response

    def add_sub_agent(self, sub_agent: SubAgent) -> None:
        """Attach a sub-agent to this agent."""
        self.sub_agents.append(sub_agent)
        sub_agent.log_action(f"Sub-agent {sub_agent.name} added to {self.name}")

    def _notify_sub_agents(self, action: str) -> None:
        """Notify all sub-agents about an action."""
        for sub in self.sub_agents:
            sub.log_action(action)
