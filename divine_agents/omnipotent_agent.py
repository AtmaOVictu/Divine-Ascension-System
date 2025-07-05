"""Module defining an OmnipotentAgent capable of supervising others."""

from __future__ import annotations

from typing import List

from .agent import Agent


class OmnipotentAgent(Agent):
    """Agent with supervision and control capabilities."""

    def __init__(self, name: str, state: str = "Ego") -> None:
        super().__init__(name, state)
        self.supervision_scope: List[Agent] = []
        self.analysis_report: List[str] = []

    def assign_supervision(self, agents: List[Agent]) -> None:
        """Assign agents to supervise."""
        self.supervision_scope = agents
        names = [agent.name for agent in agents]
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
                self.analysis_report.append(
                    f"Agent {agent.name} has neutral emotions."
                )

    def provide_feedback(self) -> str:
        """Return collected analysis as feedback."""
        if not self.analysis_report:
            return "No agents under supervision."
        return "\n".join(self.analysis_report)

    def control_transition(self, agent: Agent) -> None:
        """Direct the state of an agent when conditions require."""
        if agent.tension > 0.7:
            agent.state = "Enotnost"
            agent.history.append(f"{self.name} directed {agent.name} to state: Enotnost")
        elif agent.emotion < -0.5:
            agent.state = "Ego"
            agent.history.append(f"{self.name} directed {agent.name} to state: Ego")

