from __future__ import annotations

from typing import Iterable, List

from .agent import Agent


class OmnipotentAgent(Agent):
    """Agent with oversight and critical analysis capabilities."""

    def __init__(self, name: str, state: str = "Ego") -> None:
        super().__init__(name, state)
        self.criticality_level = 0
        self.supervision_scope: List[Agent] = []
        self.analysis_report: List[str] = []

    def assign_supervision(self, agents: Iterable[Agent]) -> None:
        """Assign agents to be supervised."""
        self.supervision_scope = list(agents)
        names = [a.name for a in self.supervision_scope]
        self.analysis_report.append(f"Assigned supervision over: {names}")

    def analyze_agents(self) -> None:
        """Analyze supervised agents and collect feedback."""
        for agent in self.supervision_scope:
            action = agent.history[-1] if agent.history else "No actions"
            if "cooperate" in action:
                self.analysis_report.append(
                    f"Agent {agent.name} is cooperative, might be guided by love."
                )
            elif "compete" in action:
                self.analysis_report.append(
                    f"Agent {agent.name} is too competitive, might be driven by hate."
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
        """Return collected feedback."""
        if not self.analysis_report:
            self.analysis_report.append("No agents under supervision.")
        return "\n".join(self.analysis_report)

    def control_transition(self, agent: Agent) -> None:
        """Direct an agent to a specific state based on tension or emotion."""
        if agent.tension > 0.7:
            agent.state = "Enotnost"
            agent.history.append(f"{self.name} directed {agent.name} to state: Enotnost")
        elif agent.emotion < -0.5:
            agent.state = "Ego"
            agent.history.append(f"{self.name} directed {agent.name} to state: Ego")
