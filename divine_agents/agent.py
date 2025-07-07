from typing import List
from .sub_agent import SubAgent


class Agent:
    """Represents an ontological agent capable of transitioning states.

    Each agent can be assisted by multiple ``SubAgent`` instances that log
    actions and help track internal state changes.
    """

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
        self._trigger_sub_agents("Emotion updated")

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self._trigger_sub_agents("Tension updated")

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            self._trigger_sub_agents(f"State transitioned to {self.state}")
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
        self._trigger_sub_agents("Response generated")
        return reply

    def add_sub_agent(self, sub_agent: SubAgent) -> None:
        """Attach a sub-agent to this agent."""
        self.sub_agents.append(sub_agent)
        sub_agent.log_action(f"Sub-agent {sub_agent.name} added to {self.name}")

    def _trigger_sub_agents(self, action: str) -> None:
        """Notify sub-agents of an action."""
        for sa in self.sub_agents:
            sa.log_action(action)
