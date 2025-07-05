from __future__ import annotations

from typing import List

from .agent import Agent


class OmnipotentAgent(Agent):
    """Agent with supervisory abilities over other agents."""

    def __init__(self, name: str, state: str = "Ego") -> None:
        super().__init__(name, state)
        self.supervision_scope: List[Agent] = []
        self.analysis_report: List[str] = []

    def assign_supervision(self, agents: List[Agent]) -> None:
        """Assign agents to be supervised."""
        self.supervision_scope = agents
        names = ", ".join(a.name for a in agents)
        self.analysis_report.append(f"Assigned supervision over: {names}")

    def analyze_agents(self) -> None:
        """Analyze supervised agents and record feedback."""
        for agent in self.supervision_scope:
            action = agent.history[-1] if agent.history else "No actions"
            if "compete" in action:
                self.analysis_report.append(
                    f"Agent {agent.name} is too competitive, might be driven by hate."
                )
            elif "cooperate" in action:
                self.analysis_report.append(
                    f"Agent {agent.name} is cooperative, might be guided by love."
                )
            else:
                self.analysis_report.append(
                    f"Agent {agent.name} is neutral, needs further analysis."
                )

            if agent.emotion < 0:
                self.analysis_report.append(
                    f"Agent {agent.name} shows negative emotions."
                )
            elif agent.emotion > 0:
                self.analysis_report.append(
                    f"Agent {agent.name} shows positive emotions."
                )
            else:
                self.analysis_report.append(f"Agent {agent.name} has neutral emotions.")

    def provide_feedback(self) -> str:
        """Return collected feedback for supervised agents."""
        if not self.analysis_report:
            return "No agents under supervision."
        return "\n".join(self.analysis_report)

    def control_transition(self, agent: Agent) -> None:
        """Force a state transition based on tension or emotion."""
        if agent.tension > 0.7:
            agent.state = "Enotnost"
            agent.history.append(f"{self.name} directed {agent.name} to state: Enotnost")
        elif agent.emotion < -0.5:
            agent.state = "Ego"
            agent.history.append(f"{self.name} directed {agent.name} to state: Ego")


class LoadingScreenUnity:
    """Represents a cyclical unity loading process."""

    def __init__(self, agent_name: str, min_value: float = 0.01, max_value: float = 1.0) -> None:
        self.agent_name = agent_name
        self.unity_value = min_value
        self.min_value = min_value
        self.max_value = max_value

    def update(self, increment: float = 0.01) -> float:
        """Increment unity value and wrap when exceeding the maximum."""
        self.unity_value += increment
        if self.unity_value > self.max_value:
            self.unity_value = self.min_value
        return self.unity_value

