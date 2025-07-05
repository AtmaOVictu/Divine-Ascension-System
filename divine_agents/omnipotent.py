# -*- coding: utf-8 -*-
"""Module implementing the OmnipotentAgent for supervising other agents."""

from __future__ import annotations

from typing import List

from .agent import Agent


class OmnipotentAgent(Agent):
    """Agent with supervisory control over other agents."""

    def __init__(self, name: str, state: str = "Ego") -> None:
        super().__init__(name, state)
        self.criticality_level: int = 0
        self.supervision_scope: List[Agent] = []
        self.analysis_report: List[str] = []

    def assign_supervision(self, agents: List[Agent]) -> None:
        """Assign agents to supervision scope."""
        self.supervision_scope = agents
        assigned = ", ".join(agent.name for agent in agents)
        self.analysis_report.append(f"Assigned supervision over: [{assigned}]")

    def analyze_agents(self) -> None:
        """Analyze supervised agents and record observations."""
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
        """Return a feedback report."""
        if not self.analysis_report:
            self.analysis_report.append("No agents under supervision.")
        return "\n".join(self.analysis_report)

    def control_transition(self, agent: Agent) -> None:
        """Direct an agent to a new state based on tension or emotion."""
        if agent.tension > 0.7:
            agent.state = "Enotnost"
            agent.history.append(f"{self.name} directed {agent.name} to state: Enotnost")
        elif agent.emotion < -0.5:
            agent.state = "Ego"
            agent.history.append(f"{self.name} directed {agent.name} to state: Ego")

    def recommend_improvement(self, agent: Agent) -> str:
        """Return a suggestion to improve agent behaviour."""
        if agent.emotion < -0.5:
            return (
                f"Agent {agent.name} needs to reduce negativity and improve cooperation."
            )
        if agent.emotion > 0.5:
            return (
                f"Agent {agent.name} is on a positive path; maintain balance and empathy."
            )
        return f"Agent {agent.name} requires further observation for tailored advice."
