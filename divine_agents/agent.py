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
        self.history.append(self.state)
        self._trigger_sub_agents(f"State transitioned to {self.state}")
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            response = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            response = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            response = "Vse resnice so eno, medsebojno povezane."
        response = self._apply_emotion_influence(response)
        self._trigger_sub_agents(f"Response generated: {response}")
        return response

    def _apply_emotion_influence(self, response: str) -> str:
        """Modify the response with an emotional tone."""
        if self.emotion > 0.7:
            return f"Z veseljem: {response}"
        if self.emotion < 0.3:
            return f"S strahom: {response}"
        return response

    def add_sub_agent(self, sub_agent: SubAgent) -> None:
        """Attach a sub-agent to this agent."""
        self.sub_agents.append(sub_agent)
        sub_agent.log_action(f"Sub-agent {sub_agent.name} added to {self.name}")

    def _trigger_sub_agents(self, action: str) -> None:
        """Notify sub-agents of an action for logging purposes."""
        for sa in self.sub_agents:
            sa.log_action(action)
