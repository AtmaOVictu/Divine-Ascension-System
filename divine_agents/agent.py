from __future__ import annotations

from typing import List

from .sub_agent import SubAgent


class Agent:
    """Ontological agent capable of state transitions and interaction."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history: List[str] = [state]
        self.sub_agents: List[SubAgent] = []

    def add_sub_agent(self, sub_agent: SubAgent) -> None:
        """Attach a sub-agent to this agent."""
        self.sub_agents.append(sub_agent)
        sub_agent.log_action(f"Sub-agent {sub_agent.name} added to {self.name}")

    def _trigger_sub_agents(self, action: str) -> None:
        """Notify all sub-agents of an action."""
        for sa in self.sub_agents:
            sa.log_action(action)

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self._trigger_sub_agents(f"Emotion updated to {value}")

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self._trigger_sub_agents(f"Tension set to {value}")

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        self._trigger_sub_agents(f"State transitioned to {self.state}")
        return self.state

    def apply_emotion_influence(self, text: str) -> str:
        """Adjust a response based on current emotion."""
        if self.emotion > 0.7:
            return f"Z veseljem: {text}"
        if self.emotion < 0.3:
            return f"S strahom: {text}"
        return text

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        reply = self.apply_emotion_influence(base)
        self._trigger_sub_agents(f"Responded: {reply}")
        return reply
