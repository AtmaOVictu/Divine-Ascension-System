from __future__ import annotations

from typing import List

from .agent import Agent


class OmnipotentAgent(Agent):
    """Agent with oversight and control over other agents."""

    def __init__(self, name: str, state: str = "Ego") -> None:
        super().__init__(name, state)
        self.criticality_level = 0
        self.supervision_scope: List[Agent] = []
        self.analysis_report: List[str] = []

    def assign_supervision(self, agents: List[Agent]) -> None:
        """Assign agents to be supervised."""
        self.supervision_scope = agents
        self.analysis_report.append(
            f"Assigned supervision over: {[agent.name for agent in agents]}"
        )

    def analyze_agents(self) -> None:
        """Analyze supervised agents and build a report."""
        self.analysis_report.clear()
        for agent in self.supervision_scope:
            last_state = agent.history[-1] if agent.history else "Unknown"
            if agent.emotion < 0:
                self.analysis_report.append(
                    f"Agent {agent.name} shows negative emotions."
                )
            elif agent.emotion > 0:
                self.analysis_report.append(
                    f"Agent {agent.name} shows positive emotions."
                )
            else:
                self.analysis_report.append(
                    f"Agent {agent.name} has neutral emotions."
                )
            self.analysis_report.append(f"Last state: {last_state}")

    def provide_feedback(self) -> str:
        """Return the collected analysis report."""
        if not self.analysis_report:
            return "No analysis available."
        return "\n".join(self.analysis_report)

    def control_transition(self, agent: Agent) -> None:
        """Directly manipulate an agent's state based on thresholds."""
        if agent.tension > 0.7:
            agent.state = "Enotnost"
            agent.history.append(f"{self.name} directed {agent.name} to Enotnost")
        elif agent.emotion < -0.5:
            agent.state = "Ego"
            agent.history.append(f"{self.name} directed {agent.name} to Ego")
